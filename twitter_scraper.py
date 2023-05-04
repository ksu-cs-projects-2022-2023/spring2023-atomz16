import tweepy
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def analyze(post):
    post = post.lower()
    tokens = word_tokenize(post)

    context_keywords = {'campus', 'program', 'engineering', 'business', 'education', 'class', 'school', 'agriculture', 'alumni'}

    for i in range(1, len(tokens)):
        if tokens[i] in context_keywords:
            return True

    return False

print("Starting Search")

# put your credential API information here (do not share your API to the public)
# API Consumer Key and Secret from Twitter
api_key = "GoFw50lpwDgecw2UNXhvJOMGy"
api_secret = "vHc3IhWcqLyEWQT4DPv2GPc6MgDzkWft5BbRnxr75vl7O3GiXL"

access_token = "951307038881144833-L2P4HbhgEZCHM41qYWL5B3lNPF3WPUg"
access_token_secret = "R9mAjVtfXXLyxuv6F1R4tFs7sB5M0dLhBmVMV3ZyaVWRv"

# authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []
for tweet in tweepy.Cursor(api.search_tweets,q="West AND Virginia AND University",
                            until='2023-04-26', #Twitter only allows to search tweets from the previous week
                            result_type='recent',
                            include_entities=True,
                            tweet_mode='extended', #otherwise it only captures 140 characters
                            lang="en").items():
    tweets.append({
        'tweet': tweet.full_text,
        'tweetID': tweet.id_str,
        'userName': tweet.user.name,
        'userLocation': tweet.user.location,
        'postTime': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'retweets': tweet.retweet_count,
        'likes': tweet.favorite_count,
    })

for tweet in tweepy.Cursor(api.search_tweets,q="west AND virginia AND university",
                            until='2023-04-26', #Twitter will automatically sample the last 7 days of data, and only allows you to get 7-day data
                            result_type='recent',
                            include_entities=True,
                            tweet_mode='extended', #otherwise it only captures 140 characters
                            lang="en").items():
    tweets.append({
        'tweet': tweet.full_text,
        'tweetID': tweet.id_str,
        'userName': tweet.user.name,
        'userLocation': tweet.user.location,
        'postTime': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'retweets': tweet.retweet_count,
        'likes': tweet.favorite_count,
    })


for tweet in tweepy.Cursor(api.search_tweets,q="WVU OR wvu",
                            until='2023-04-26', #Twitter will automatically sample the last 7 days of data, and only allows you to get 7-day data
                            result_type='recent',
                            include_entities=True,
                            tweet_mode='extended', #otherwise it only captures 140 characters
                            lang="en").items():
    tweets.append({
        'tweet': tweet.full_text,
        'tweetID': tweet.id_str,
        'userName': tweet.user.name,
        'userLocation': tweet.user.location,
        'postTime': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'retweets': tweet.retweet_count,
        'likes': tweet.favorite_count,
    })
"""
for tweet in tweepy.Cursor(api.search_tweets,q="oklahoma AND state",
                            until='2023-04-26', #Twitter will automatically sample the last 7 days of data, and only allows you to get 7-day data
                            result_type='recent',
                            include_entities=True,
                            tweet_mode='extended', #otherwise it only captures 140 characters
                            lang="en").items():
    tweets.append({
        'tweet': tweet.full_text,
        'tweetID': tweet.id_str,
        'userName': tweet.user.name,
        'userLocation': tweet.user.location,
        'postTime': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'retweets': tweet.retweet_count,
        'likes': tweet.favorite_count,
    })


for tweet in tweepy.Cursor(api.search_tweets,q="OKState OR OKstate OR Okstate OR okstate",
                            until='2023-04-26', #Twitter will automatically sample the last 7 days of data, and only allows you to get 7-day data
                            result_type='recent',
                            include_entities=True,
                            tweet_mode='extended', #otherwise it only captures 140 characters
                            lang="en").items():
    tweets.append({
        'tweet': tweet.full_text,
        'tweetID': tweet.id_str,
        'userName': tweet.user.name,
        'userLocation': tweet.user.location,
        'postTime': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'retweets': tweet.retweet_count,
        'likes': tweet.favorite_count,
    })
"""
print(len(tweets))

with open("wvu_posts.json", "w") as outfile:
    json.dump(tweets, outfile, indent=4)