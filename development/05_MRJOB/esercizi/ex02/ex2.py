from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 2
# From the lorem.txt file calculate how many words starts for each letter of the alphabet and print out the max and the min.


class MREx_02(MRJob):
    def steps(self):
        return []

    def mapper_lettercount(self, _, line):
        pass

    def reducer_lettercount(self, something, something_else):
        pass


if __name__ == '__main__':
    MREx_02.run()
