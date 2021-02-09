# this example downloads a public google spreadsheet and sniffs though any matched tweets
import csv
from io import StringIO

import requests
import tweepy

import db
from musk_sniffer import musk

response = requests.get(
    'https://docs.google.com/spreadsheets/u/3/d/1ghxQzjuZ6LpkgsnS4gpvEkhSY0KYAWt0C72tHZ0rFew/export?format=csv')
# UI version https://docs.google.com/spreadsheets/d/1ghxQzjuZ6LpkgsnS4gpvEkhSY0KYAWt0C72tHZ0rFew/edit?usp=sharing
assert response.status_code == 200, 'Wrong status code'
f = StringIO(response.content.decode())
reader = csv.reader(f, delimiter=',')
headers = next(reader, None)

print("Get your key and secret from https://developer.twitter.com/en/portal/dashboard")
auth = tweepy.AppAuthHandler(consumer_key="#TODO", consumer_secret="#TODO")

api = tweepy.API(auth)
tweet_db = db.tweetdb(db_name="something1.db")


def cb(keyword, text, tweet):
    """
    :param keyword: list of keywords matched
    :param text: Plantext tweet that matched the string
    :param tweet : https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
    :return:
    """
    # TODO implement slack notifier here
    print(keyword)
    print(text)
    print(tweet)
    tweet_url = "https://twitter.com/{handler}/status/{id}".format(id=tweet.id, handler=tweet.user.screen_name)
    print(tweet_url)


for row in reader:
    # print(row[0]) # rows ['handler', 'keyword', 'tweet']
    account = musk(whom=row[0], says=row[1].split(","), api=api, database=tweet_db, callback=cb)
    account.sniff(count=50)
