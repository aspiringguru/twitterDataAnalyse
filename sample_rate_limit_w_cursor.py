"""

"""
import sys
import tweepy
import time
from random import randint

from keys import keys #keep keys in separate file, keys.py
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    c = tweepy.Cursor(api.followers_ids, id = 'McDonalds')
    print "type(c)=", type(c)
    ids = []
    for page in c.pages():
        ids.append(page)
    print "ids=", ids
    print "ids[0]=", ids[0]
    print "len(ids[0])=", len(ids[0])
    print 5/0

except tweepy.TweepError:
    print "tweepy.TweepError="#, tweepy.TweepError
except:
    e = sys.exc_info()[0]
    print "Error: %s" % e
    #print "error."

