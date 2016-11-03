from mrjob.job import MRJob
from mrjob.step import MRStep
import re

## Exercise 3
# Write a MapReduce job that report the most frequent word grouped by word length.

WORD_REGEXP = re.compile(r"[\w']+")

class MREx_03(MRJob):
    def steps(self):
        return []


if __name__ == '__main__':
    MREx_03.run()
