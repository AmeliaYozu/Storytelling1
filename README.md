# StreamingDataStart
Storytelling coursework1

I chose Twitter Streaming as my incoming source, each data represent a Tweet sent by a person. Each individual message can fall into 3 parts:

<b>1. Tweet Information</b>

the first several lines mainly represent the Tweet's key contents:
	
for example (picked from stream): 
		
		"text": "I'm at @RedLobster in Hicksville, NY https://t.co/6xWjTrYCXa", 
		"is_quote_status": false,  
		"in_reply_to_status_id": null, 
		"id": 696145090327220224, 
		"coordinates": {"type": "Point", "coordinates": [-73.52765454, 40.77712828]},
		"favorite_count": 0,
		"retweet_count": 0, 
		"in_reply_to_user_id": null, 
		"lang": "en", 
		"in_reply_to_status_id_str": null,
		"created_at": "Sun Feb 07 01:34:57 +0000 2016", 
We knows from the data about the Tweet. It is created at Feb 07 1:34(GTC time), pretty close the time when I captured it in stream so which make sense it shows that the Tweet has not been "liked". The context is about the user who tweeted this is at RedLobster and at Hicksville, NY. There is no quoted Tweet in this Tweet and the user is not replying to someone. And the Tweet is created at the location shown above as a coordinate.

There is an other important element is "entities", in which contains some "elements" embeded in this Tweet, just like if the user mentioned someone, who is it, if there is a hashtag in it, what is it. Shown as below:

		"user_mentions": [{"id": 6018732,"indices": [7,18], "id_str": "6018732", "screen_name": "redlobster", "name": "Red Lobster"], 
		"symbols": [], 
		"hashtags": [], 
		"urls": []

<b>2. User Information</b>

There is an element "user", which includes the user's information:

		"followers_count": 136, 
		"id": 246633733, 
		"statuses_count": 5001,
		"description": "Just a girl trying to make a name for herself in this big world of ours. Look out for me promoting mental health awareness and the stigmas attached to them.", 
		"friends_count": 90,
		"location": "Queens", 
		"name": "Nicole Jeremiah", 
		"favourites_count": 28, 
		"screen_name": "Linamerie", 
		"lang": "en", 
		"created_at": "Thu Feb 03 04:35:50 +0000 2011", 
		"time_zone": "Pacific Time (US & Canada)", 
		
Based on these information, we knows the basic information about the user. It is a she. Her name is Nicole and her "Twitter name" is Linamerie. Primary language is English. She lives in is Queens, NYC. She created this Twitter account in 2011. Her time is Pacific Time. She has 90 friends currently on Twitter, and has tweeted 5001 Tweets, but only has 136 followers.
	
There are some other information contained in User field, like the user's configuration about her profile, like the background, the profile photo, whether she enabled geo service and some other settings.
	
<b>3. Geo Location Information</b>

		"full_name": "Hicksville, NY", 
		"country": "United States", 
		"place_type": "city", 
		"bounding_box": {
		"type": "Polygon", 
		"coordinates": [[[-73.560512, 40.743142], [-73.560512, 40.793139], [-73.499673, 40.793139],[-73.499673,40.743142]]]}, 
		"country_code": "US", 
		"attributes": {}, 
		"id": "48b5e9defad76941", 
		"name": "Hicksville"
		}

This is the detailed geo location infomation for this Tweet. It indicates that the Tweet is created at Hicksville with a geo location bounding in a specific region. And Hicksville is in NY, US.

<b>The raw data is included in 'example.txt' file.</b>
 
 
