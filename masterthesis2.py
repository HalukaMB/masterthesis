from twython import Twython
import csv

consumerkey = "SYvzgBXUzR3ikkbyKFbcc2Xil"

tokenkey=""

Token=csv.reader(open("token.csv","r"))
for line in Token:
    print((line.strip("[")))
    tokenkey= str(line)


twitter = Twython(consumerkey, access_token=tokenkey)

results= twitter.search(q='Theresa May', result_type='popular')

for line in results:
    print(line)
