import sys
import csv
import tweepy
import time
from random import randint

from keys import keys #keep keys in separate file, keys.py
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)




countTotal = 0
countValue = 0
trigger = 100

if len(sys.argv)<2:
    inputFile = raw_input("input file name: ")
else:
    inputFile = str(sys.argv[1])

#inputFile = 'ZoukAtlantafollowers.txt'
print "loading twitter data from csv file ", inputFile
#outputFile = "blah.txt" #inputFile+"_"+str(trigger)
#fo = open(outputFile,'w')

with open(inputFile, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        countTotal += 1
        #print "username=", row[0], " followers=", int(row[1]), ", ",int(row[1])>trigger," status count=", int(row[2]),", ", int(row[2])>trigger
        if (int(row[1])>100) & (int(row[2])>100):
            #user.followers_count>100 & user.statuses_count>100 = likely high value user
            print "username=", row[0], " followers=", int(row[1]), ", ",int(row[1])>trigger," status count=", int(row[2]),", ", int(row[2])>trigger
            countValue += 1
            #fo.write(row[0]+"\n")
            api.create_friendship(row[0])
            sleepTime = 60+randint(0,3)*60+randint(0,60)
            print "now following user ", row[0], " sleeping for ", sleepTime, "seconds"
            time.sleep(sleepTime)

print "\ncountTotal=", str(countTotal), ", countValue=", str(countValue)
#fo.close()


"""
http://docs.tweepy.org/en/v3.5.0/api.html
"""