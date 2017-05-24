from twython import Twython
import datetime
import time
import csv

consumerkey = "SYvzgBXUzR3ikkbyKFbcc2Xil"

tokenkey=""

Token=csv.reader(open("token.csv","r"))
for line in Token:
    print(str(line))
    tokenkey=((str(line)).replace("'", "").replace("[", "").replace("]", ""))
    print(tokenkey)


twitter = Twython(consumerkey, access_token=tokenkey)
Corbyn=csv.writer(open("resultsCorbyn.csv","w"))
results = twitter.cursor(twitter.search, q='Corbyn', count="100")
for result in results:
    print(result)
    Corbyn.writerow([str(result)])

params = {'count':200, 'contributor_details':True}
home = twitter.get_home_timeline(**params)

def handle_rate_limiting():
    app_status = {'remaining':1} # prepopulating this to make the first 'if' check fail
    while True:
        if app_status['remaining'] &gt; 0:
            status = twitter.get_application_rate_limit_status(resources = ['statuses', 'application'])
            app_status = status['resources']['application']['/application/rate_limit_status']
        else :
            wait = max(app_status['reset'] - time.time(), 0) + 10
            time.sleep(60*15)

def otherfunction:
    while True:
        try:
            newest = None
            params = {'count':200, 'contributor_details':True, 'since_id':latest}
            handle_rate_limiting()
            home = twitter.get_home_timeline(**params)
            if home:
                while home:
                    store_tweets(home)

                    if newest is None:
                        newest = True
                        latest = home[0]['id']

                    params['max_id'] = home[-1]['id'] - 1
                    handle_rate_limiting()
                    home = twitter.get_home_timeline(**params)
            else:
                time.sleep(60)

        except TwythonRateLimitError, e:
            print "[Exception Raised] Rate limit exceeded"
            reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
            wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
            time.sleep(wait)
        except Exception, e:
            print e
            print "Non rate-limit exception encountered. Sleeping for 15 min before retrying"
            time.sleep(60*15)
