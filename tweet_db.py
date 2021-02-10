import sqlite3


class tweetdb:
    def __init__(self, db_name="twitter_squeezer.db"):

        self.con = sqlite3.connect(db_name)

        self.con.row_factory = sqlite3.Row
        self.initialize_table("test")

    def table_exists(self, table_name):

        cur = self.con.cursor()
        cur.execute("select count(*) from sqlite_master where type='table' and name=(?)", [table_name])
        return cur.fetchone()[0] == 1

    def initialize_table(self, table_name):
        if (self.table_exists(table_name)):
            return

        create_table_statement = {

            "create_stream_table": "create table if not exists " + table_name + " (id varchar primary key, text varchar)"
            # TODO sql injection YOLO
        }

        for key in create_table_statement:
            try:
                with self.con:
                    self.con.execute(create_table_statement[key])
            except sqlite3.OperationalError as e:
                print("couldn't add the tables twice")
                print(e)
            except Exception as e:
                message = "An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args)
                print(message)

    def add_tweet(self, status):
        with self.con:
            user = status.user.screen_name
            text = status.text
            id = status.id
            self.con.execute("INSERT INTO " + user + " VALUES (?,?)", (id, text))
            self.con.commit()
