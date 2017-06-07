import json
import csv
import io

'''
creates a .csv file using a Twitter .json file
the fields have to be set manually
'''

data_json = io.open('JeremyTheresa_tweets_new.json', mode='r', encoding='utf-8').read() #reads in the JSON file
data_python = json.loads(data_json)

csv_out = io.open('JeremyTheresa_tweets_new_out_utf8.csv', mode='w', encoding='utf-8') #opens csv file


fields = u'created_at,text,screen_name,followers,friends,rt,fav' #field names
csv_out.write(fields)
csv_out.write(u'\n')

for line in data_python:

    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
    row = [line.get('created_at'),
           '"' + line.get('text').replace('"','""') + '"', #creates double quotes
           line.get('user').get('screen_name'),
           (line.get('user').get('followers_count')),
           (line.get('user').get('friends_count')),
           (line.get('retweet_count')),
           (line.get('favorite_count'))]
    print(str(row))
    row_joined = (str(row).strip('[').strip(']'))
    print(row_joined)
    csv_out.write(row_joined)
    csv_out.write(u'\n')




csv_out.close()
