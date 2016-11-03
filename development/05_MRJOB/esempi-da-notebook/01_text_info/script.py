from mrjob.job import MRJob
import re
WORD_REGEXP = re.compile(r"[\w']+")

class MRTextInfo(MRJob):
    def mapper(self, _, line):
        for phrase in line.split('.'):
            yield 'phrases', 1
            words = WORD_REGEXP.findall(phrase)
            for word in words:
                yield 'words', 1
                yield 'characters', len(word)

    def reducer(self, key, counts):
        yield key, sum(counts)


if __name__ == '__main__':
    try:
        MRTextInfo.run()
    except TypeError:
        print 'MrJob cannot work inside iPython Notebook as it is not saved as a standalone .py file'
       


