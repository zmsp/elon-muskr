import sqlite3

import tweepy

import tweet_db as tweetDB


class Account:
    def __init__(self, whom="elonmusk", when="", says=["doge", "btc"], callback=None, api=None,
                 database=None):
        # Get your key and secret from https://developer.twitter.com/en/portal/dashboard
        self.whom = whom
        self.api = api
        self.says_what = says
        self._callback = callback
        self.says = says
        print(database)

        if database:
            print("init")
            self.db = database
            self.db.initialize_table(table_name=whom)

    def extract(self, count=10):
        for tweet in tweepy.Cursor(self.api.user_timeline, id=self.whom).items(count):

            if self.db:
                try:
                    self.db.add_tweet(tweet)
                except  sqlite3.IntegrityError as e:

                    continue
            word_list = []

            for keyword in self.says:
                matcher_word = keyword.strip().lower()
                if matcher_word in ["", " ", ","]:
                    continue
                if matcher_word == "*" or matcher_word in tweet.text.lower():
                    word_list.append(keyword)
            if (word_list.__len__() > 0):
                if (self._callback):
                    self._callback(word_list, tweet.text, tweet)


if __name__ == '__main__':
    import argparse

    print("Get your key and secret from https://developer.twitter.com/en/portal/dashboard")

    parser = argparse.ArgumentParser()
    parser.add_argument("key")
    parser.add_argument("secret")
    parser._positionals.title = 'Positional arguments'

    args = parser.parse_args()
    auth = tweepy.AppAuthHandler(args.key, args.secret)

    api = tweepy.API(auth)
    database = tweetDB.tweetdb(db_name="fun.db")


    def cb(keyword, text, tweet):
        "We execute this function when specific keyword is matched"
        print("MATCHED")
        print(keyword)
        print(text)


    accounts = [Account(whom="elonmusk", says=["a"], api=api, database=database, callback=cb),
                Account(whom="littleBIGCoder", says=["*"], api=api, database=database, callback=cb)]
    for a in accounts:
        a.extract(5)
