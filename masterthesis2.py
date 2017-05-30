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
        Corbyn.write(str(result))
        count+=1
