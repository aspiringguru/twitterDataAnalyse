"""
not working at moment. publishing for review.
"""
import tweepy #redundant due to use of from blah import bleagh
import time #use for delay
import csv #use for read/write to .csv files
import ConfigParser
import json


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from nltk.chat import eliza

config = ConfigParser.ConfigParser()


from keys import keys #keep keys in separate file, keys.py
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#uses rate limiter to prevent banning/dropping by twitter.

chatbot = eliza.Chat(eliza.pairs)

class ReplyToTweet(StreamListener):

    def on_data(self, data):
        print data
        tweet = json.loads(data.strip())

        retweeted = tweet.get('retweeted')
        from_self = tweet.get('user',{}).get('id_str','') == account_user_id

        if retweeted is not None and not retweeted and not from_self:

            tweetId = tweet.get('id_str')
            screenName = tweet.get('user',{}).get('screen_name')
            tweetText = tweet.get('text')

            chatResponse = chatbot.respond(tweetText)

            replyText = '@' + screenName + ' ' + chatResponse

            #check if repsonse is over 140 char
            if len(replyText) > 140:
                replyText = replyText[0:139]+"..."

            print('Tweet ID: ' + tweetId)
            print('From: ' + screenName)
            print('Tweet Text: ' + tweetText)
            print('Reply Text: ' + replyText)

            # If rate limited, the status posts should be queued up and sent on an interval
            #twitterApi.update_status(status=replyText, in_reply_to_status_id=tweetId)
            api.update_status(status=replyText, in_reply_to_status_id=tweetId)

    def on_error(self, status):
        print status

print "A"
streamListener = ReplyToTweet()
print "streamListener=", streamListener
twitterStream = Stream(auth, streamListener)
print "twitterStream=", twitterStream
twitterStream.userstream(_with='user')
print "B=end"