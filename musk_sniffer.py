import sqlite3

import tweepy

import db as tweetDB


class musk:
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

    def sniff(self, count=20):
        for tweet in tweepy.Cursor(self.api.user_timeline, id=self.whom).items(count):
            if self.db:
                try:
                    self.db.add_tweet(tweet)
                except  sqlite3.IntegrityError as e:
                    continue
            word_list = []

            for keyword in self.says:
                if keyword.lower() in tweet.text.lower():
                    word_list.append(keyword)

            if (word_list.__len__() > 0):
                print("MATCHED" + word_list.__str__())
                if (self._callback):
                    self._callback(keyword, tweet.text, tweet)


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
        print(keyword)
        print(text)


    smell = [musk(whom="elonmusk", api=api, database=database, callback=cb),
             musk(whom="littleBIGCoder", api=api, database=database, callback=cb)]
    for i in smell:
        i.sniff()
