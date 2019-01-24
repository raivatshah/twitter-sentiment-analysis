import tweepy
from textblob import TextBlob

#Create your app from apps.twitter.com and fill your keys
consumer_key = 'xyz'
consumer_secret = 'xyz'
access_token = 'xyz'
access_token_secret = 'xyz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#asks user for input. Makes program more usable. 
public_tweets = api.search(input("Enter keyword(s)"))

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print('\n')