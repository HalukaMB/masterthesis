from twython import TwythonStreamer

class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print (data['text'].encode('utf-8'))

    def on_error(self, status_code, data):
        print (status_code)
        self.disconnect()

# replace these with the details from your Twitter Application
consumer_key = 'srD1uUvn2KKmhCwi97z1QIjC4'
consumer_secret = 'I5AjT9k3jtemrvi4On2RU9IsWX6lZ5fBUd8tOmbD97OwYkn0UR'
access_token = '460957118-867428375383728129csqa2QQc7AaR2RM8QS1T3EcvpGPXXAN'
access_token_secret = 'PtsUKOlm3kcRnh5WRkrCdRDHMjO4XePJdKmzh8mrKnXUg'



streamer = TweetStreamer(consumer_key, consumer_secret,
                         access_token, access_token_secret)

streamer.statuses.filter(track = 'Theresa May')
