# this example downloads a public google spreadsheet and sniffs though any matched tweets
import csv
import json
import os
from io import StringIO

import requests
import tweepy
from conf import *

from tweet_db import tweetdb
from twitter_squeezer import Account




## setup datagbase


def send_to_slack(message):
    """
    Sends message to slack
    :param message:
    """

    if debug:
        print(message)
        return True
    else:
        slack_data = {'text': message, 'channel': slack_channel, "username": slack_username,
                      "icon_emoji": slack_icon_emoji}

        response = requests.post(
            slack_webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'},
            proxies=proxyDict
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )


def cb(keywords, text, tweet):
    """
    :param keyword: list of keywords matched
    :param text: Plantext tweet that matched the string
    :param tweet : https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
    :return:
    """
    # TODO implement slack notifier here
    tweet_url = "https://twitter.com/{handler}/status/{id}".format(id=tweet.id, handler=tweet.user.screen_name)
    message = " *{user}* _ {text} _ ` {url} ` _ matched: {keyword}_".format(keyword=','.join(keywords), text=text,
                                                                            url=tweet_url, user=tweet.user.screen_name)
    send_to_slack(message)




## setup tweetpy
"Get your key and secret from https://developer.twitter.com/en/portal/dashboard"



auth = tweepy.AppAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
api = tweepy.API(auth)

##  download google spreadsheet
response = requests.get(csv_url)

assert response.status_code == 200, 'Wrong status code'
f = StringIO(response.content.decode())
reader = csv.reader(f, delimiter=',')
headers = next(reader, None)

tweet_db = tweetdb(db_name="test.db")

for row in reader:
    t = Account(whom=row[0], says=row[1].split(","), api=api, database=tweet_db, callback=cb)
    t.extract(count=15)
