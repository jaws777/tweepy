import tweepy


# Replace bearer token value with your own
bearer_token = ""

# Initializing the Tweepy client
client = tweepy.Client(bearer_token)

# Replace user ID
id = 2244994945

# By default the Tweet ID and Tweet text will be returned.
tweets = client.get_users_tweets(id)

# Print the Tweet id
for tweet in tweets.data:
    print(tweet.id)
    