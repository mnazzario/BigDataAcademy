import tweepy
import time
from datetime import datetime as dt
from pymongo import MongoClient

class IntesaTweets(object):
    def __init__(self, auth):
        self.auth = auth
        self.api = tweepy.API(self.auth)
        self.intesa_cursor = tweepy.Cursor(self.api.user_timeline, screen_name='intesasanpaolo')

    def get_tweets(self):
        while True:
            try:
                yield self.intesa_cursor.pages().next()
            except tweepy.RateLimitError:
                print "[LOG %s] Timeout reached.. I'm going to sleep for 15 minutes.." % dt.now()
                time.sleep(15 * 60)
                print "[LOG %s] Try Again!" % dt.now()
            except StopIteration as st:
                print "[LOG %s] Stop Iteration " % dt.now()
                break
            except Exception as e:
                # Generic Exception
                print "[LOG %s] Generic error " % dt.now()
                print "[LOG %s] Wait 60 seconds..." % dt.now()
                time.sleep(60)


print "[LOG %s] STARTING" % dt.now()

# SETUP TWITTER
CONSUMER_KEY = "UkTIiyST8qNhL0dRTYguXw"
SECRET_KEY = "qowanEGNLxOD8p8EqNtzcTQUD3o0RQLaGffY5XZ7jVI"
ACCESS_TOKEN = "775822357-Skbuj2JaQ8PBAUmiZ0R5oOYn0OmMiZuyXONkhn8D"
SECRET_ACCESS_TOKEN = "X3ryjErVyYIcLsaAlbsZ6ERz2iBJK4hArbU1vsbI"

auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)

api = tweepy.API(auth)

# SETUP PYMONGO
client = MongoClient('mongodb://localhost:27017/')
db = client.intesa

intesa = api.get_user('intesasanpaolo')
db.intesa.insert(intesa._json)

print "[LOG %s] Script Completed!" % dt.now()
