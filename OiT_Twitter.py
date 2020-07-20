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
nrTweets = 10

search = 'outintech' # Phrase to search for

# Comment on tweets
comment = 'Hey! @OutInTech has a Slack channel with over 13,000 LGBTQ+ professionals worldwide. Thought you might be interested in joining our active & inclusive Slack channel + meet new friends & supporters around the world. bit.ly/Slack-OIT'

# Searching for phrase amongst tweets and commenting on them
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print('Commented')
        api.update_status(comment, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)        
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
