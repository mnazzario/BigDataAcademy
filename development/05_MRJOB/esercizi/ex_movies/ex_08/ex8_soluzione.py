from mrjob.job import MRJob

# Exercise 8
# Count occurrences of rating value from movie DB.

class MRRatingCounter(MRJob):

    def mapper(self, key, value):
        (userID, movieID, rating, timestamp) = value.split('\t')
        yield rating, 1

    def reducer(self, rating, occurrences):
        yield rating, sum(occurrences)


if __name__ == '__main__':
    MRRatingCounter.run()
