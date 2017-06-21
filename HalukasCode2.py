from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from redis import Redis
from rq import Queue
import requests
import time
import io
import os
import json
import threading
import multiprocessing
from datetime import datetime, timedelta
import _credentials

# twitter OAuth
ckey = _credentials.ckey
consumer_secret = _credentials.consumer_secret
access_token_key = _credentials.access_token_key
access_token_secret = _credentials.access_token_secret


#Listener Class Override
class listener(StreamListener):

    def __init__(self, start_time, time_limit):
        self.time = start_time
        self.limit= time_limit
        self.tweet_data = []



    def on_data(self, data):
        while (time.time() - self.time) < self.limit:
            try:
                self.tweet_data.append(data)
                return True

            except BaseException:
                print ('failed ondata')
                time.sleep(5)
                pass

        print(u'[\n')
        print(','.join(self.tweet_data))
        print(u'\n]')
        exit()



    def on_error(self, status):

        print (status)

    def on_disconnect(self, notice):

        print ('bye')




#Beginning of the specific code
keyword_list = ['Theresa May', 'Jeremy Corbyn', 'GE2017', 'Labour', 'Tory','Tories'] #track list

start_time=time.time()
auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener
