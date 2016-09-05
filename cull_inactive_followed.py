import sys
import tweepy
import time
from random import randint
from keys3 import keys #keep keys in separate file, keys.py
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# config section START - do NOT edit.
myScreenName = 'InspiredGuruAu'
# config section END - do NOT edit.

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    usersInfo = api.get_user(myScreenName)
    #print ("usersInfo=", usersInfo)
    print ("type(usersInfo)=", type(usersInfo))
    print ("usersInfo.id=", usersInfo.id)
    print ("usersInfo.name=", usersInfo.name)
    print ("usersInfo.screen_name=", usersInfo.screen_name)
    print ("usersInfo.created_at=", usersInfo.created_at)
    print ("usersInfo.description=", usersInfo.description)
    print ("usersInfo.followers_count=", usersInfo.followers_count)
    friends = api.friends_ids(api.me().id)
    print("You follow", len(friends), "users")
    print ("friends[0:10]=", friends[0:10])
    count = 0
    newFollowedCount = 0
    followers = []#list of people who follow myScreenName
    for user in tweepy.Cursor(api.followers, screen_name=myScreenName).items():
        #print ("user.screen_name=", user.screen_name, "user.id=", user.id, " type(user)=", type(user))
        followers.append(user.id)
        #if user.id not in friends, create friendship.
        if user.id not in friends:
            print ("\nuser.id=", user.id, " is following you, but you are not following them.\n")
            #http://docs.tweepy.org/en/v3.5.0/api.html#API.create_friendship
            #API.create_friendship(id/screen_name/user_id[, follow])
            try:
                api.create_friendship(user.id)
                print ("followed user.id=", user.id, "\n")
                newFollowedCount += 1
            except tweepy.TweepError:
                print("error when api.create_friendship(", user.id, "), tweepy.TweepError=", tweepy.TweepError)
    #now test if the accounts I follow are following me.
    friendNotFollowingCount = 0
    for friend in friends:
        #test if friend is in followers
        if friend not in followers:
            print ("friend not in followers")
            friendNotFollowingCount += 1
            try:
                print ("'friend' with id=", friend, " is not following you, friendNotFollowingCount=", friendNotFollowingCount)
                api.destroy_friendship(friend)
            except tweepy.TweepError:
                print ("error in api.destroy_friendship(friend) tweepy.TweepError=", tweepy.TweepError)
    #print ("followers=", followers)
    #print ("friends=", friends)
    print("You follow", len(friends), "users")
    print ("friendNotFollowingCount=", friendNotFollowingCount)
    print ("newFollowedCount=", newFollowedCount)
    print ("len(followers)=", len(followers))



except tweepy.TweepError:
    print ("tweepy.TweepError=", tweepy.TweepError)
    print ("followers=", followers)
    print ("friends=", friends)
    print("You follow", len(friends), "users")
    print ("friendNotFollowingCount=", friendNotFollowingCount)
    print ("newFollowedCount=", newFollowedCount)
    print ("len(followers)=", len(followers))
except Exception as e:
    print ("general exception ", e)



