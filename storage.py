import io
tweet_data=[]
def storage(data):
      saveFile = io.open('JeremyTheresa_tweets_new.json', 'a', encoding='utf-8')


      tweet_data.append(data)





      saveFile = io.open('JeremyTheresa_tweets_new.json', 'w', encoding='utf-8')
      saveFile.write(u'[\n')
      saveFile.write(','.join(tweet_data))
      saveFile.write(u'\n]')
      saveFile.close()
      print("END!")
      exit()
