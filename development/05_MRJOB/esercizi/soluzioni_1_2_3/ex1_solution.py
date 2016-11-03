from mrjob.job import MRJob
from mrjob.step import MRStep
import re

# Exercise 1
# From the lorem.txt file calculate how many words starts for each letter of the alphabet.

WORD_REGEXP = re.compile(r"[\w']+")

class MREx_01(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_lettercount,
                    reducer=self.reducer_lettercount)
        ]

    def mapper_lettercount(self, _, line):
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w.lower()[0], 1

    def reducer_lettercount(self, letter, counts):
        yield letter, sum(counts)  # Sum occurrences of each word to get frequency


if __name__ == '__main__':
    MREx_01.run()
