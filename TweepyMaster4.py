from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# twitter OAuth
ckey = 'szIul7ZRYlIoYB3Vp5kyyj42u'
consumer_secret = 'MG18KBN61TY5adittIJRweMzsjxnhspXSKmhMZuMGweYqlheUR'
access_token_key = '867428375383728129-cmzkW7Y66ioJcWhOt420O1MBiyWygVU'
access_token_secret = 'tAdBBmW16j2nTwBMMPT8ZlgqGUmgzR9SRtwbDRkUDiXZL'


#Listener Class Override
class listener(StreamListener):

    def on_data(self, data):
        print(data)

    def on_error(self, status):

        print (status)

    def on_disconnect(self, notice):

        print ('bye')


#Beginning of the specific code
keyword_list = ['cardiff'] #track list

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener()) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener
