"""
get info about a user
"""
import sys
import tweepy
import time
from random import randint
from keys2 import keys #keep keys in separate file, keys.py
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

from config import config #keep configuration values in separate file, config.py
inputFilename = config['inputFilename']
minSleepTime = config['minSleepTime']
maxSleepTime = config['maxSleepTime']
print ("inputFilename=", inputFilename)
print ("minSleepTime=", minSleepTime)
print ("maxSleepTime=", maxSleepTime)
# config section START - do NOT edit.
myScreenName = "peterjamessmit6" #'InspiredGuruAu'
maxTweetCharLength = 140
danceTagsFileName = "danceTags.txt"
#inputFilename = "danceQuotes.txt"
#minsleepTime & maxsleepTime in seconds.
#minSleepTime = 1 #reccomend min sleep time 300 seconds (5 minutes),
# 3600 seconds (30 minutes is more practical. Nobody likes a spammer
#maxSleepTime = 2 #maxSleepTime can be as large as you want.
# config section END

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    print ("marker2")
    """
    usersInfo = api.get_user("myScreenName")
    print ("usersInfo=", usersInfo)
    print ("type(usersInfo)=", type(usersInfo))
    print ("usersInfo.id=", usersInfo.id)
    print ("usersInfo.name=", usersInfo.name)
    print ("usersInfo.screen_name=", usersInfo.screen_name)
    print ("usersInfo.created_at=", usersInfo.created_at)
    print ("usersInfo.description=", usersInfo.description)
    print ("usersInfo.followers_count=", usersInfo.followers_count)
    print ("usersInfo._json=", usersInfo._json)
    print ("type(usersInfo._json)=", type(usersInfo._json) )
    print ("usersInfo._json['profile_image_url_https']=", usersInfo._json["profile_image_url_https"] )
    """
    quotes = []
    print ("marker2xx")
    for line in open(inputFilename, encoding="utf8"):
        #print ("ss")
        #time.sleep(1)
        try:
            line = line.rstrip('\n')
            line = line.strip()  # the while loop will leave a trailing space, 
              # so the trailing whitespace must be dealt with
              # before or after the while loop
            while '  ' in line:
                line = line.replace('  ', ' ')
            print ("line=", line.encode("utf-8"))
            if len(line)<=maxTweetCharLength:
                quotes.append(line)
        except Exception as e:
            print ("general exception ", e)
    print ("len(quotes)=", len(quotes))

    danceTags = []
    for line in open(danceTagsFileName):
        #print ("line=", line)
        #time.sleep(1)
        try:
            line = line.rstrip('\n')
            print ("line=", line)
            if len(line)<=maxTweetCharLength:
                danceTags.append(line)
        except Exception as e:
            print ("general exception ", e)
    print ("len(danceTags)=", len(danceTags))
    print ("danceTags=", danceTags)

    while True:
        try:
            randQuote = randint(0,len(quotes)-1)
            randQuoteTxt = quotes[randQuote]
            randTag = danceTags[randint(0, len(danceTags))]
            print ("randTag=", randTag)
            if len(randQuoteTxt+" #"+randTag)<maxTweetCharLength:
                randQuoteTxt = randQuoteTxt+" #"+randTag
            print ("tweeting ", randQuoteTxt)
            api.update_status(randQuoteTxt)
            sleepTime = randint(minSleepTime,maxSleepTime)
            print ("sleeping for ", sleepTime, "seconds")
            time.sleep(sleepTime)
        except tweepy.TweepError:
            print ("tweepy.TweepError=", tweepy.TweepError)
        except Exception as e:
            print ("general exception ", e)

except tweepy.TweepError:
    print ("tweepy.TweepError=", tweepy.TweepError)
except Exception as e:
    print ("general exception ", e)


"""
http://docs.tweepy.org/en/v3.5.0/api.html#API.update_status
"""