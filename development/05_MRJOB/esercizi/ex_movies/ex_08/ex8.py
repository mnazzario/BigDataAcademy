from mrjob.job import MRJob

# Exercise 8
# Count occurrences of rating value from movie DB.

class MRRatingCounter(MRJob):

    def mapper(self, key, value):
        pass

    def reducer(self, something, something_else):
        pass


if __name__ == '__main__':
    MRRatingCounter.run()
