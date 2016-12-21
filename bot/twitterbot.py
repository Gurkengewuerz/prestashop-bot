import tweepy
import time
from config import *


class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)


if __name__ == "__main__":
    twitter = TwitterAPI()
    while True:
        twitter.tweet("", "")
        time.sleep(1)
