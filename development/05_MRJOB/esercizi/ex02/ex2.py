from mrjob.job import MRJob
from mrjob.step import MRStep

import re

WORD_REGEXP = re.compile(r"[\w']+")
# Exercise 2
# From the lorem.txt file calculate how many words starts for each letter of the alphabet and print out the max and the min.


class MREx_02(MRJob):
    def steps(self):
            return [
                MRStep(mapper=self.mapper_lettercount,
                       reducer=self.reducer_lettercount),
                MRStep(mapper=self.mapper_findminmax,
                       reducer=self.reducer_findminmax)
            ]
        
    def mapper_lettercount(self, _, line):
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w[0].lower(), 1

    def reducer_lettercount(self, word, counts):
         yield word, sum(counts)
    
    def mapper_findminmax(self, word, freq):
        yield 'min', [freq, word]
        yield 'max', [freq, word]
    
    def reducer_findminmax(self, key, freqs):
        #for v in freqs:
        #    print v
        if key=='min':
            yield "MIN", min(freqs)
        else:
            yield "MAX", max(freqs)
        #print key
        #print max(freqs)
        #print max(freqs)
        #yield 1,1
    
if __name__ == '__main__':
    MREx_02.run()

    
