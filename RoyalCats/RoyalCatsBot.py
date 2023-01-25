
import tweepy
import json
import os.path
import time
from datetime import datetime
import sys
import requests

from KEYSnotforpublic import royalcatskeys as rck

####################################

def api():
    auth = tweepy.OAuthHandler(rck.api_key, rck.api_secret)
    auth.set_access_token(rck.access_token, rck.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    api.update_status_with_media(message, image_path)

    print("tweeted successfully")


# if __name__ == "__main__":
#     api = api()
#     ## tweet(api, #"this was tweeted from python"-message, #imagepath????)
