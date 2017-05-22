from twython import Twython
import csv

consumerkey = "SYvzgBXUzR3ikkbyKFbcc2Xil"

consumersecret = "slxu8jP9cvT4AILDF3jijEkwk2uMqFUkhn9PPv2rAqqlerLuTE"




twitter = Twython(consumerkey, consumersecret,  oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

print(ACCESS_TOKEN)

Token=csv.writer(open("token.csv","w"))
Token.writerow([ACCESS_TOKEN])
