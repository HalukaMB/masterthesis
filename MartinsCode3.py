import time
import threading
import multiprocessing

from twython import TwythonStreamer, Twython
from datetime import datetime, timedelta

from db_cache import *
from _credentials import *
from _sources import sources
from json_file_cache import TwitterFileCache

#Defines to update user list whenever a time difference of 24 hours is present
UPDATE_USER_LIST = timedelta(hours=24)
#Defines to update profile  whenever a time difference of 6 hours is present
UPDATE_PROFILES = timedelta(hours=6)


# deal with streaming updates
class Streamer(TwythonStreamer):

    def __init__(self, cache, *args):
        """
        Initialise a connection to a database
        to store returned tweets in
        """
        #sets up the db_cache
        self.db_cache = cache
        #initializes the TwythonStreamer and arguments are passed on
        TwythonStreamer.__init__(self, *args)

    def on_success(self, data):
        """
        Add a tweet to the database
        """
        #WHAT IS THIS DOING?!?
        self.db_cache.put_document('tweets', data)

    def on_error(self, status_code, data):
        """
        Output any errors
        """
        #Prints the status code of an error and the retrieved data
        print(status_code)
        print(data)

    #disconnect and ends the stream
    def end_stream(self):
        self.disconnect()


class StreamMonitor(object):

    def __init__(self):

        # file cache of twitter responses
        self.file_cache = TwitterFileCache()
        # DB cache
        self.db_cache = MongoDBCache(db='MediaMonitor')
        # API object for accessing Twitter API
        self.ts = Streamer(self.db_cache, twitter_client_id, twitter_client_secret, twitter_access_token, twitter_access_token_secret)
        # users
        self.users = ""

    def read_users(self):
        #stores all users from the db_cache in u
        u = self.db_cache.get_collection('users')
        #empty list
        us = []
        # each users id in u is appended to the us list
        for user in u:
            us.append(user['id_str'])
        #list is appended to the empty users element of self
        self.users = ','.join(us)
        #length of list is returned
        return len(us)

    def monitor_stream(self, users=None):
        #always is true
        if users is None:
            #the users from self object is used
            users = self.users
        #gives the self object a filter that filters out only users from self
        #and only tweets in english
        self.ts.statuses.filter(follow=users, lang="en")

    def disconnect_stream(self):
        #ends the stream
        self.ts.end_stream()


class ProfileMonitor(object):

    def __init__(self):
        # file cache of twitter responses
        self.file_cache = TwitterFileCache()
        # DB cache
        self.db_cache = MongoDBCache(db='MediaMonitor')
        # Twitter API
        self.ta = Twython(twitter_client_id, twitter_client_secret, twitter_access_token, twitter_access_token_secret)

        # query limiting
        max_per_hour = 175 * 15
        query_interval = (60 * 60) / float(max_per_hour)   # in seconds

        self.monitor = {'wait': query_interval,
                        'earliest': None,
                        'timer': None}

    def __rate_controller(self, monitor_dict):
        if monitor_dict['timer'] is not None:
            monitor_dict['timer'].join()   # causes main thread to sit and wait

            # Waste time in the (unlikely) case that the timer thread finished early.
            while time.time() < monitor_dict['earliest']:
                time.sleep(monitor_dict['earliest'] - time.time())

        # Prepare for next call and start timer...
        earliest = time.time() + monitor_dict['wait']
        timer = threading.Timer(earliest-time.time(), lambda: None)
        monitor_dict['earliest'] = earliest
        monitor_dict['timer'] = timer
        monitor_dict['timer'].start()

    def update_profiles(self):
        u = self.db_cache.get_collection('users')
        users = []
        for user in u:
            users.append(user['id_str'])

        start = 0
        end = 0

        while end < len(users):
            start = end
            if end + 99 < len(users):
                end = end + 99
            else:
                end = len(users)

            ids = ",".join(users[start:end])
            user_content = self.query_user_lookup(ids)
            for user in user_content:
                if user["protected"] != 'true':
                    self.file_cache.put_profile(user)
                    self.db_cache.put_document('users', user)

    def query_user_lookup(self, ids):
        self.__rate_controller(self.monitor)
        user_content = self.ta.lookup_user(user_id=ids)

        if self.ta.get_lastfunction_header('x-rate-limit-remaining') == 0:
            self.monitor['earliest'] = float(self.ta.get_lastfunction_header['x-rate-limit-reset'])
            return self.query_user_lookup(ids)
        else:
            return user_content

#First line of code that gets executed right away
if __name__ == "__main__":

#defines the both streams (see above)
    sm = StreamMonitor()
    pm = ProfileMonitor()

#counts to start with the number of user in the db_cache using the defined function "read_users"
    print("updating user list")
    num_users = sm.read_users()
    print("currently tracking: %d" % (num_users))

#another run process is initiated for the monitor_stream function with the multiprocessing package
    p = multiprocessing.Process(target=sm.monitor_stream)

#sets the daemon for this process to true (so this will run always)
    p.daemon = True
    print("starting stream")
#background process is started
    p.start()

#start times of the stream are set
    profile_check_time = datetime.today()
    user_list_check_time = datetime.today()

#This While loop will run forever
    while(True):
        #Retrieves the time as of now
        current_time = datetime.today()
        #Checks the difference between starting time and current time,
        #if it is bigger than 6 hours, this if will be executed
        if current_time - profile_check_time > UPDATE_PROFILES:
            print("updating profiles")
            #profile stream is updated with the "update_profiles" function
            pm.update_profiles()
            print("profiles updated")
            #start time for the profile check is reset
            profile_check_time = datetime.today()

        #if it is bigger than 24 hours, this if will be executed
        current_time = datetime.today()
        if current_time - user_list_check_time > UPDATE_USER_LIST:
            print("killing stream")
            #stream monitor is terminated
            p.terminate()
            print("currently tracking: %d" % (num_users))
            print("updating user list")
            #number of users updated
            num_users = sm.read_users()
            print("now tracking: %d" % (num_users))

            #same process as up there started
            user_list_check_time = datetime.today()
            p = multiprocessing.Process(target=sm.monitor_stream)
            p.daemon = True
            print("starting stream")
            p.start()
    p.join()
