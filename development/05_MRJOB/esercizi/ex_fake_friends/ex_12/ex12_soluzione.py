__author__ = 'alexcomu'
from mrjob.job import MRJob

# EX 12

# For each Age -> Avarage of friends

# CSV Structure:
# ID, Name, Age, Number of Friends


class MRAvarageFriends(MRJob):

    def mapper(self, key, value):
        # Extract ages and number of friends
        (userID, name, age, nFriends) = value.split(',')
        yield age, float(nFriends)

    def reducer(self, age, nFriends):
        # calculate for each age the avarage of friends
        total = 0
        numElements = 0
        for num in nFriends:
            total += num
            numElements += 1
        yield age, total / numElements


if __name__ == '__main__':
    MRAvarageFriends.run()
