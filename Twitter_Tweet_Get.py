from tweepy import Stream
from tweepy import OAuthHandler #For handling authentication
from tweepy.streaming import StreamListener #For streaming tweets
import json
from pymongo import MongoClient
import pymongo

# Credentials that are generated in the Twitter developer app

access_token = '12407609509********************'
access_token_secret = 'cvqK********************'
consumer_token = 'gM8j******************'
consumer_token_secret = '2zv6zc**************'

client = MongoClient()
db = client.kaushal
tweet_collection = db.CIS612_2
tweet_collection.create_index([("id", pymongo.ASCENDING)], unique=True)

class Listen(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        tweet_collection.insert_one(tweet)
        return True

if __name__ == "__main__":
    listener = Listen()  # listener object of Listener class
    authentication = OAuthHandler(consumer_token, consumer_token_secret)
    authentication.set_access_token(access_token, access_token_secret)
    stream = Stream(authentication, listener)  # stream object with authentication
    stream.filter(track=["Presidential Election", "Donald Trump", "Joe Biden"])  # filtering the tweets with




