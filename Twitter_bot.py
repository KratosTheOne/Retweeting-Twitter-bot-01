# This is the Main file which runs the script to Retrieve tweets.
# Tweepy is an Easy-to-use python library for accessing the Twitter API.

import tweepy
import time
import keys

# The keys are imported from keys.py file.
key1 = keys.C_K
key2 = keys.C_S
key3 = keys.A_K
key4 = keys.A_S

print('This is a Twitter bot')

CONSUMER_KEY = key1
CONSUMER_SECRET = key2
ACCESS_KEY = key3
ACCESS_SECRET = key4

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


# The below two functions are used to retrieve and store the last official tweet id.
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


FILE_NAME_FAV = 'last_fav_tweet_id'


# The function looks for the mentioned id and likes and retweets it back.
# The @USERID is where the user will add his T
def fav_tweet():
    print('Retrieving tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME_FAV)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")
    for mention in reversed(mentions):
        if not mention:
            return
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_fav_tweet = mention.id
        store_last_seen_id(last_fav_tweet, FILE_NAME_FAV)
        print('found @kaustubh_sinha1', flush=True)
        print('fav-ing and retweeting tweet...', flush=True)
        api.create_favorite(mention.id)
        api.retweet(mention.id)


# The script keeps running with a time delay of 10 secs till the user stops the program.
while True:
    fav_tweet()
    time.sleep(10)
