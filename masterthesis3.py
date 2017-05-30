from twython import Twython
import csv
import json
import io

consumerkey = "SYvzgBXUzR3ikkbyKFbcc2Xil"

tokenkey=""

Token=csv.reader(open("token.csv","r"))
count=0
for line in Token:
    print(str(line))
    tokenkey=((str(line)).replace("'", "").replace("[", "").replace("]", ""))
    print(tokenkey)


twitter = Twython(consumerkey, access_token=tokenkey)
status = twitter.get_application_rate_limit_status(resources = ['statuses'])
print(status)
#home_status = status['resources']['statuses']['/statuses/home_timeline']
#app_status = status['resources']['application']['/application/rate_limit_status']
#print(home_status)
#print(app_status)
Corbyn=io.open('raw_tweets.json', 'a', encoding='utf-8')
results = twitter.cursor(twitter.search, q='Corbyn', count= '100')
for result in results:
    if count>200:
        break
    else:
        Corbyn.write(u'[\n')
        Corbyn.write(str(result))
        Corbyn.write(u'\n]')
        count+=1

Corbyn.close()

data_json = open('raw_tweets.json', mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object


csv_out = open('tweets_out_ASCII.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
writer.writerow(fields) #writes field

for line in data_python:

    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
    writer.writerow([line.get('created_at'),
                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     line.get('user').get('screen_name'),
                     line.get('user').get('followers_count'),
                     line.get('user').get('friends_count'),
                     line.get('retweet_count'),
                     line.get('favorite_count')])

csv_out.close()
