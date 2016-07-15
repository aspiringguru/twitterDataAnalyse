"""
started from http://www.tulane.edu/~howard/CompCultES/twitter.html
"""

# -*- coding: utf-8 -*-
# suggested name: tweepyFlujoMonitor
import tweepy
from tweepy.api import API


from keys import keys # requires keys.py file, see example in repo.
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
key = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#some fluff for demo purposes.
user = tweepy.API(key).me()
print('user.name=' + user.name)
print('user.id=' + str(user.id))
print('user.screen_name=' + user.screen_name)
print('user.location=' + user.location)
print('str(user.friends_count))=' + str(user.friends_count))
print('user.created_at=' + str(user.created_at))
print('user.favourites_count=' + str(user.favourites_count))
print('user.followers_count=' + str(user.followers_count))
print('user.friends_count=' + str(user.friends_count))
print('user.id_str=' + user.id_str)
print('user.listed_count=' + str(user.listed_count))
print('user.location=' + user.location)
print('user.statuses_count=' + str(user.statuses_count))

outputFile_id = "streamingIDstore.txt"
f_id = open(outputFile_id,'w')
outputFile_status = "streamingStatusStore.txt"
f_status = open(outputFile_status,'w')



class Stream2Screen(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 20

    def on_id(self, id):
        print str(id)
        f_id.write(str(id))

    def on_location(self, location):
        print (location)
"""
    def on_status(self, status):
        print status.text.encode('utf8')
        f_status.write(status.text.encode('utf8'))
        self.n = self.n+1
        if self.n < self.m: return True
        else:
            print 'tweets = '+str(self.n)
            return False
"""




stream = tweepy.streaming.Stream(key, Stream2Screen())
#stream.filter(track=['de'], languages=['es'])
stream.filter(track=['salsa'], languages=['en'], stall_warnings=True)
print ("end")



"""
https://dev.twitter.com/streaming/overview/request-parameters
'the twitter' is the AND twitter, and 'the,twitter' is the OR twitter).
todo: set async for terminating stream safely
http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html
myStream.filter(track=['python'], async=True)

https://github.com/tweepy/tweepy/blob/master/tests/test_streaming.py
"""