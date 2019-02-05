import tweepy
import sys

consumer_key = '51PkpfAxfIPUMCqcw8bf8w8iI'
consumer_secret = 'C27gFe3loVbWwyU9XzyEARMn2398xQ5GJQykDzxx8zlrIedHzx'

access_token = '2486856455-4jqktHbZYnCK6dUGbbR3KmyL7Qkopuz509CQ3na'
access_token_secret = '7URcWwdqXIjfSLoRclFY3Vf6hRZIhQbIDYe5aMjWX2ohw'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


public_tweets = tweepy.Cursor(api.search, q=sys.argv[1], lang="pt" ,tweet_mode="extended").items(int(sys.argv[2]))

for tweet in public_tweets:
    print('Registro inserido com sucesso !')
    print(tweet.full_text)
    

