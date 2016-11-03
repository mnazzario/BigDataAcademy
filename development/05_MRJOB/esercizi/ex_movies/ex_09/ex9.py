__author__ = 'alexcomu'
from mrjob.job import MRJob
from mrjob.step import MRStep

# Ex 9 - Most Rated Movie

class MRMostRatedMovie(MRJob):

    def steps(self):
        return []

    def get_movies_rating(self, key, value):
        pass

    def reducer_movie_rating(self, movieID, occurrences):
        pass


if __name__ == '__main__':
    MRMostRatedMovie.run()
