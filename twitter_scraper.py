import tweepy
import pandas as pd
import datetime
import string
tweets = [] #initialize an empty list

api_key = "GoFw50lpwDgecw2UNXhvJOMGy"
api_secret = "vHc3IhWcqLyEWQT4DPv2GPc6MgDzkWft5BbRnxr75vl7O3GiXL"

access_token = "951307038881144833-L2P4HbhgEZCHM41qYWL5B3lNPF3WPUg"
access_token_secret = "R9mAjVtfXXLyxuv6F1R4tFs7sB5M0dLhBmVMV3ZyaVWRv"

# authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split()[0])

for status in tweepy.Cursor(api.search_tweets,q="K-State",
                            until=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split()[0], #Twitter will automatically sample the last 7 days of data, and only allows you to get 7-day data
                            result_type='recent',
                            include_entities=True,
                            tweet_mode='extended', #otherwise it only captures 140 characters
                            lang="en").items(100):
    
    #post_time = status.created_at # tweets posting time
    tweet = status.full_text # gets the tweets texts
    #screenName = status.user.screen_name
    likes = status.favorite_count
    
    if (likes > 25):
        tweets.append((tweet, likes))
        print("\n-------------------------------------------------------------------------\n" +
                "----------------------------Tweet----------------------------------------\n" +
                "-------------------------------------------------------------------------\n\n")
        print(tweet)


