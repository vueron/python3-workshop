import tweepy
consumer_key = "something"
consumer_secret = "something"
access_token = "something"
access_token_secret = "something"

auth =tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,compression=True)


message_string = "my bot's first tweet"
api.update_status(message_string)
