"""
modified by aspiringguru from
https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
also referencing
http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html#a-few-more-pointers
https://dev.twitter.com/overview/api/response-codes
https://dev.twitter.com/rest/public/rate-limiting
https://dev.twitter.com/streaming/overview
"""
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import ast

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
from keys import keys # requires keys.py file, see example in repo.
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

count =0
pausetime = 0

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:
            print(data)
            #print ("type(data)=", type(data))
            d = ast.literal_eval(data)
            print ("type(d)=", type(d))
            #print ("data.id=", data.id, "\ndata.text=", data.text)
            #count += 1
        except Exception, e:
            print ("Exception, e=", e)#trapping malformed string error here.
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            #420	Enhance Your Calm = you are being rate limited.
            pausetime += 60
            print ("status == 420, pausing for ", pausetime, " seconds")
            time.sleep(pausetime)
            # pause using timer.
        elif status == 429:
            #429	Too Many Requests =  rate limit has been exhausted
            print ("status == 429, Too Many Requests. This is bad.")

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'], async=True)
