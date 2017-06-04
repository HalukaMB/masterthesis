from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import io
import os
import json
import threading
import multiprocessing
from datetime import datetime, timedelta



# twitter OAuth
ckey = 'szIul7ZRYlIoYB3Vp5kyyj42u'
consumer_secret = 'MG18KBN61TY5adittIJRweMzsjxnhspXSKmhMZuMGweYqlheUR'
access_token_key = '867428375383728129-cmzkW7Y66ioJcWhOt420O1MBiyWygVU'
access_token_secret = 'tAdBBmW16j2nTwBMMPT8ZlgqGUmgzR9SRtwbDRkUDiXZL'


#Listener Class Override
class listener(StreamListener):

    def __init__(self):
        self.count = 0

    def on_data(self, data):

        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
        saveFile.write(data)
        self.count += 1
        print(self.count)
        if self.count>50:
            self.on_disconnect("notice")




    def on_error(self, status):

        print (status)

    def on_disconnect(self, notice):

        print ('bye')


#Defines to update user list whenever a time difference of 24 hours is present
UPDATE_USER_LIST = timedelta(seconds=30)

sm = listener()

p=multiprocessing.Process(target=sm.on_data)
p.daemon=True
print("Start the stream")
p.start()

#Beginning of the specific code
keyword_list = ['Theresa May'] #track list

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
twitterStream = Stream(auth, listener()) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener
