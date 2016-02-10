from TwitterAPI import TwitterAPI
import json
import time
from sys import stdout
from sys import stdin

CONSUMER_KEY = '8aIDWdGQuFgC9oypr2yozz6KY'
CONSUMER_SECRET = 'tn3FJdxt22QrHgim07mmaWOxFhNCtj7BB3pAjNVEw9aVZyECWC'
ACCESS_TOKEN_KEY = '4883184502-tPuS4S7rC0gEqpGq08EFtkUo1HYTZbskez2YtYu'
ACCESS_TOKEN_SECRET = '0xS7drlYHYb32ASOCEeeVo8Qx405RAreGkv0S2ARNsVLz'


api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)


r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
for item in r:		
#To filter tweets with location information
#        if item['place']['name']=='Manhattan' and item['geo']!= None:
	if item['geo']!= None:
        	username = item['user']['screen_name']
        	text = item['text']
        	timestamp = item['timestamp_ms']
        	t = int(timestamp[:-3])
        	attime = time.ctime(t)
        	place = item['place']['full_name']+", "+item['place']['country']
        	co = item['coordinates']['coordinates'] #array
        	print username+ ": " +text+"\n"+attime+"\n"+place+"\n"+str(co)
       		#print json.dumps(item, indent=1)
       		stdout.flush()
       		print "##################################################"
