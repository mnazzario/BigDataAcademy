__author__ = 'alexcomu'
from mrjob.job import MRJob

# EX 12

# For each Age -> Avarage of friends

# CSV Structure:
# ID, Name, Age, Number of Friends


class MRAvarageFriends(MRJob):

    def mapper(self, key, value):
        pass

    def reducer(self, age, nFriends):
        pass


if __name__ == '__main__':
    MRAvarageFriends.run()
