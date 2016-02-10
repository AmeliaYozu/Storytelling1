from TwitterAPI import TwitterAPI
import json
import time
from sys import stdout
from sys import stdin
from alchemyapi import AlchemyAPI

#Tweet Streaming API Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''


#Use AlchemyAPI to get sentiment analysis #need API key, which is stored in api_key.txt
alchemyapi = AlchemyAPI()

#connect to TwitterAPI, ready to get stream!
api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

#get stream here with specified location filter to only get Tweets from New York
r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})

#Handling each received json format Tweet:
#Extract userID, user name, Tweet content, Tweet time&location information and sentiment analysis result
#for each Tweet text, as 'mood'.
#
for item in r:
  if item['geo']!= None:
    username=item['user']['screen_name']#get userID
    uname= item['user']['name']#get user name
    text = item['text']#get Tweet text

    #get and format timestamp into readable time string
    timestamp = item['timestamp_ms']
    t = int(timestamp[:-3])
    attime = time.ctime(t)

    #get location information: city, state, country and coordinate
    place = item['place']['full_name']+", "+item['place']['country']
    co = item['coordinates']['coordinates'] #array

    #get sentiment information of Tweet text
    feature = alchemyapi.sentiment('text', text)['docSentiment']['type'];
    mood = ""
    if str(feature) == "positive":
      mood = str(" (^_^) ")
    else:
      if str(feature) == "negative":
        mood = str(" (T_T) ")
      else:
        mood = str("-_-")

    print "========================================================================================"
    #processed information to further send out from server
    strs = "\n"+uname+" ( "+username +") *"+mood+"* : " +text+"\n"+attime+"\n"+place+"\n(Coordinates: "+str(co)+")\n"
    print str(strs.encode('utf-8'))
    stdout.flush()

    