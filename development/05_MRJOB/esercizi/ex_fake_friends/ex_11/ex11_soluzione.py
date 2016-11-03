__author__ = 'alexcomu'
from mrjob.job import MRJob

# EX 12

# For each Age -> Avarage of friends

# CSV Structure:
# ID, Name, Age, Number of Friends


class MRMostPopular(MRJob):

    def mapper(self, key, value):
        # Extract friends and number of friends
        (userID, name, age, nFriends) = value.split(',')
        yield "MAX", (int(nFriends), int(userID))
        yield "MIN", (int(nFriends), int(userID))

    def reducer(self, key, value):
        if key == "MAX":
            yield max(value)
        else:
            yield min(value)


if __name__ == '__main__':
    MRMostPopular.run()
