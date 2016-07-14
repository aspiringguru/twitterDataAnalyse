"""
NOTE: most twitter users will have 'direct messages from anyone' turned off. Likely to breach twitter TOS.
todo:
1. read search term from user input
2. option to read list of keywords from file. NB: combinations of keywords will yield more targetted result.
3. use timers to limit messages/time unit.
4. track messages sent to users, manage # messages sent per time period.
5. combine with pre-assembled list of vetted active accounts.
"""

import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys # requires keys.py file, see example in repo.

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = api.me()
print('user.name=' + user.name)
print('user.location=' + user.location)
print('str(user.friends_count))=' + str(user.friends_count))


twts = api.search(q="some search text")#
#http://docs.tweepy.org/en/v3.5.0/api.html?highlight=search#API.search
#NB: options to search for other criteria including geocode.

#list of specific strings we want to check for in Tweets
t = ['zouk']

count = 0#do not change.
#for s in twt:
#print "type(twts)=",type(twts)
#print "twts=\n", str(twts)
for s in twts:
    for i in t:
        sn = s.user.screen_name
        try:
            print "tweet matching criteria by user=",sn, "s.text=", str(s.text)
            count += 1
            if count<=0:#modify with care, runs zero times at moment.
                m = "some message."
                api.send_direct_message(sn, m)
                print "message sent"
            else:
                print "max messages sent. no more messages."
        except UnicodeEncodeError:
            print "UnicodeEncodeError caught"
            #NB: need to manage this error better.
        except tweepy.TweepError:
            print "TweepError caught"
print "end"
"""
originally from tutorial below. Modified to make work.
- incorrect/deprecated methods used. [cannot find examples of the deprecated methods in original]
- invalid variable names used.
- try/except added to trap errors.
- rate limiting added.
- changed importing keys method
http://www.dototot.com/reply-tweets-python-tweepy-twitter-bot/
"""