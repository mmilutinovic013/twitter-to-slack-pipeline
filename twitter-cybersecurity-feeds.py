import tweepy
import requests
import json

# Twitter API credentials
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_SECRET = 'your_twitter_access_secret'

# Slack webhook URL
SLACK_WEBHOOK_URL = 'your_slack_webhook_url'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

# Search query for cybersecurity tweets
query = 'cybersecurity'

# Fetch recent tweets
tweets = api.search_tweets(q=query, count=5)

# Prepare messages and send to Slack
for tweet in tweets:
    message = {
        'text': f"{tweet.user.name} tweeted: {tweet.text}"
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(message), headers=headers)
