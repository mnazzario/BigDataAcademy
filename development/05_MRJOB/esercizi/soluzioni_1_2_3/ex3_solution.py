from mrjob.job import MRJob
from mrjob.step import MRStep
import re


WORD_REGEXP = re.compile(r"[\w']+")


class MREx_03(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_wordcount,
                    reducer=self.reducer_wordcount),
            MRStep(mapper=self.mapper_most,
                    reducer=self.reducer_most)
        ]

    def mapper_wordcount(self, __, line):
        words = WORD_REGEXP.findall(line)
        for w in words:
            if len(w)>3:
                yield w.lower(), 1

    def reducer_wordcount(self, word, counts):
        yield word, sum(counts)

    def mapper_most(self, word, freq):
        yield len(word), [freq, word]

    def reducer_most(self, lengroup, freqs):
        yield lengroup, max(freqs)


if __name__ == '__main__':
    MREx_03.run()
