"""
http://stackoverflow.com/questions/31000178/how-to-get-large-list-of-followers-tweepy
ask user for account name to harvest follower names from.
print follower names to screen
pause  users to screen
"""
import tweepy
import time
import csv

import sys

if len(sys.argv)<2:
    accountvar = raw_input("Account name: ")
else:
    accountvar = str(sys.argv[1])

if accountvar[0]=="@":
    print "stripping leading @ from username"
    accountvar = accountvar[1:]
#todo: upgrade this to read usernames from a file.
print "searching for followers of "+accountvar


from keys import keys #keep keys in separate file, keys.py
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#refer http://docs.tweepy.org/en/v3.2.0/api.html#API
#tells tweepy.API to automatically wait for rate limits to replenish


users = tweepy.Cursor(api.followers, screen_name=accountvar).items()
count = 0
errorCount=0

outputfile = accountvar+"followers.txt"
outputfilecsv = accountvar+"followers.csv"
f = open(outputfile,'w')
fc = csv.writer(open(outputfilecsv, 'wb'))

while True:
    try:
        user = next(users)
        count += 1
        #use count-break during dev to avoid twitter restrictions
        #if (count>10):
        #    break
    except tweepy.TweepError:
        #catches TweepError when rate limiting occurs, sleeps, then restarts.
        #nominally 15 minnutes, make a bit longer to avoid attention.
        print "sleeping...."
        time.sleep(60*16)
        user = next(users)
    except StopIteration:
        break
    try:
        print "@" + user.screen_name + " has " + str(user.followers_count) +\
              " followers, has made "+str(user.statuses_count)+" tweets and location=" +\
              user.location+" geo_enabled="+str(user.geo_enabled)+" count="+str(count)
        f.write(user.screen_name+", "+str(user.followers_count)+", "+
                str(user.statuses_count)+", "+str(user.geo_enabled)+"\n")
        fc.writerow([user.screen_name, str(user.followers_count), str(user.statuses_count), user.location, str(user.geo_enabled)])
    except UnicodeEncodeError:
        errorCount += 1
        print "UnicodeEncodeError,errorCount ="+str(errorCount)

f.close()
#apparently don't need to close csv.writer.
print "completed, errorCount ="+str(errorCount)+" total users="+str(count)
    #print "@" + user.screen_name
    #todo: write users to file, search users for interests, locations etc.

"""
http://docs.tweepy.org/en/v3.5.0/api.html?highlight=tweeperror#TweepError
NB: RateLimitError inherits TweepError.
http://docs.tweepy.org/en/v3.2.0/api.html#API  wait_on_rate_limit & wait_on_rate_limit_notify
NB: possibly makes the sleep redundant but leave until verified.

todo: add log file functions to record triggers of wait_on_rate_limit & error messages.

"""