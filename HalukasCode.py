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



# twitter OAuth
ckey = 'szIul7ZRYlIoYB3Vp5kyyj42u'
consumer_secret = 'MG18KBN61TY5adittIJRweMzsjxnhspXSKmhMZuMGweYqlheUR'
access_token_key = '867428375383728129-cmzkW7Y66ioJcWhOt420O1MBiyWygVU'
access_token_secret = 'tAdBBmW16j2nTwBMMPT8ZlgqGUmgzR9SRtwbDRkUDiXZL'


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

        saveFile = io.open('JeremyTheresa_tweets_new.json', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        print("END!")
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
twitterStream = Stream(auth, listener(start_time, time_limit=10)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener
