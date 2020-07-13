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

search = ['outintech'] # Phrase to search for

# Message to reply to tweets
message = 'Hey! @OutInTech has a Slack channel with over 13,000 LGBTQ+ professionals worldwide. Thought you might be interested in joining our active & inclusive Slack channel + meet new friends & supporters around the world. bit.ly/Slack-OIT'

# Searching for phrase amongst tweets
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        api.update_status(status = message, in_reply_to_status_id = tweet.id_str)
        print('Commented') # Indicates tweet is replied to
        tweet.favorite()
        print('Favorited') # Indicates tweet is favorited
        time.sleep(20) # Mini break
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
