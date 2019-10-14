import tweepy
consumer_key ="somevalue"
consumer_secret ="somevalue"
access_token = "somevalue"
access_token_secret = "somevalue"



auth =tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,compression=True)

username="vueron_ai"
usr_main=api.get_user(username)

follower_num =usr_main.followers_count

friend_num=usr_main.friends_count
print("followers:",follower_num)

print("friends:",friend_num)
