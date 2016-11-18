'''
Creare uno streaming Live di tweets usando le Twitter API.
'''

import tweepy


class BDStreamingListener(tweepy.StreamListener):
    def __init__(self, count):
        super(BDStreamingListener, self).__init__()

        # Number of tweets we want to retrieve
        self.count = count

    def on_status(self, status):
        # print dir(status)
        print dict(user=status.user.screen_name, text=status.text)

        self.count -= 1
        if self.count <= 0:
            return False

    def on_error(self, status_code):
        print "Error with status code: ", status_code
        return False


CONSUMER_KEY = "UkTIiyST8qNhL0dRTYguXw"
SECRET_KEY = "qowanEGNLxOD8p8EqNtzcTQUD3o0RQLaGffY5XZ7jVI"
ACCESS_TOKEN = "775822357-Skbuj2JaQ8PBAUmiZ0R5oOYn0OmMiZuyXONkhn8D"
SECRET_ACCESS_TOKEN = "X3ryjErVyYIcLsaAlbsZ6ERz2iBJK4hArbU1vsbI"


auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)

# Create an instand set the number of tweets we want ro retrieve
listener = BDStreamingListener(100)

# Create the stream fetching object with auth and listener
stream = tweepy.streaming.Stream(auth, listener)

# Tun the stream using filter
stream.filter(track=['Trump'])


