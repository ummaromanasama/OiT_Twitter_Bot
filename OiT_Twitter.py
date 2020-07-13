# #Import modules
import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# This will make the rest of the code obey the rate limit
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# Number of tweets to like
nrTweets = 5

search_1 = ['@outintech'] # Phrase to search for

# Searching for phrase amongst tweets
for tweet in tweepy.Cursor(api.search, search_1).items(nrTweets):
    try:
        print('Liked')
        tweet.favorite()
        time.sleep(20)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search_2 = ['#outintech']

for tweet in tweepy.Cursor(api.search, search_2).items(nrTweets):
    try:
        print('Hearted')
        tweet.favorite()
        time.sleep(20)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
