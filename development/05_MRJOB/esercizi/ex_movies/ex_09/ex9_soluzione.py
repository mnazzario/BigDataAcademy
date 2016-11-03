__author__ = 'alexcomu'
from mrjob.job import MRJob
from mrjob.step import MRStep

# Ex 9 - Most Rated Movie

# Calculate rating for each movie
# And return most rated

# Process:
# Apply first mapping to map movie and occurrences
# First reducer: Prepare a list of tuple (Occurrences, movieID)

# Example:
# [(1,1), (2,3), (3,2)]

# Second reducer: Extract the max value from the queue, in this case:
# (2,3)

class MRMostRatedMovie(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.get_movies_rating,
                   reducer=self.reducer_movie_rating),
            MRStep(reducer=self.reducer_output)
        ]

    def get_movies_rating(self, key, value):
        (userID, movieID, rating, timestamp) = value.split('\t')
        yield movieID, 1

    def reducer_movie_rating(self, movieID, occurrences):
        # prepare a list of tuple
        yield None, (sum(occurrences), movieID)

    def reducer_output(self, _, values):
        # max value from th queue of tuple
        yield max(values)


if __name__ == '__main__':
    MRMostRatedMovie.run()
