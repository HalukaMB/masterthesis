```
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# twitter OAuth
ckey = 'uv4CtOCc49BYDqLmFEdKag'
consumer_secret = 'OOG4ZFzY1j2uJdIzwJldIyKtp7pCEdAKxWKn2DokKY'
access_token_key = '14699651-On7JZCkV1c5K7cMpgZafmNNVaJgwVxIYjy6SGi1G2'
access_token_secret = 'N0g9NGVE9SvxoS9gqhzK7zox5EBzlR6tYguyDPG0'


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
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener```
