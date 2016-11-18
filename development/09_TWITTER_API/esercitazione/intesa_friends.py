'''
Creare uno script che recuperi da Twitter tutti i follower dell'account intesasanpaolo e salvi i dati
all'interno di una collection di MongoDB


From FRIENDS_IDS --> for each user call GET_USER
'''

import tweepy
import time
from datetime import datetime as dt
from pymongo import MongoClient


class IntesaFriends(object):

    def __init__(self, auth):
        self.auth = auth
        self.api = tweepy.API(self.auth)
        self.intesa = self.api.get_user('intesasanpaolo')

    def get_friends(self):
        for friend_id in self.api.friends_ids('intesasanpaolo'):
            try:
                yield self.api.get_user(friend_id)
            except tweepy.RateLimitError:
                print "[LOG %s] Timeout reached.. I'm going to sleep for 15 minutes.." % dt.now()
                time.sleep(15*60)
                print "[LOG %s] Try Again!" % dt.now()
            except Exception as e:
                # Generic Exception
                print "[LOG %s] Generic error " % dt.now(), e
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

intesa = IntesaFriends(auth)

print "[LOG] Twitter Setup Complete"

# SETUP PYMONGO
client = MongoClient('mongodb://localhost:27017/')
db = client.intesa

counter = 0
for friend in intesa.get_friends():
    counter += 1
    print "[LOG %s ] Friend: %s" % (dt.now(), counter)
    db.friend.insert(friend._json)

print "[LOG %s] Script Completed!" % dt.now()
