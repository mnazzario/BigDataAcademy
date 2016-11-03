from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_REGEXP = re.compile(r"[\w']+")


class MRMostFreqWord(MRJob):
    # Dichiaro i vari Step
    # Una lista di oggetti MRStep()
    def steps(self):
        return [
            MRStep(mapper=self.mapper_wordcount,
                    reducer=self.reducer_wordcount),
            MRStep(mapper=self.mapper_freq,
                    reducer=self.reducer_freq),
            MRStep(mapper=self.mapper_most,
                    reducer=self.reducer_most)
        ]

    def mapper_wordcount(self, _, line):
        words = WORD_REGEXP.findall(line)
        # Conto le parole di lunghezza maggiore a 3
        for w in words:
            if len(w)>3:
                yield w.lower(), 1

    def reducer_wordcount(self, word, counts):
        yield word, sum(counts)  # Conto le occorrenze di ogni parola per ricavare la frequenza

    def mapper_freq(self, word, total):
        if total > 1:  # Valuto solo le parole che compaiono piu di una volta
            yield total, word  # Le raggruppo per numero di occorrenze

    def reducer_freq(self, total, words):
        # Avra all'interno di total il numero di occorrenze
        # e all'interno di words un generatore che resituira le singole parole
        yield total, words.next()  # .next() restituisce il primo elemento, emetto quindi una sola parola per ogni frequenza

    def mapper_most(self, freq, word):
        yield 'most_used', [freq, word]  # Raggruppo le parole per una lista di tuple (frequenza, parola)

    def reducer_most(self, _, freqs):
        yield 'most_used', max(freqs)  # restituisco il max della lista di tuple
        # in questo caso il max verra calcolato su tutti i primi elementi delle tuple
        # di conseguenza il max() dara come risultato la frequenza piu alta e la parola associata


if __name__ == '__main__':
    try:
        MRMostFreqWord.run()
    except TypeError:
        print 'MrJob cannot work inside iPython Notebook as it is not saved as a standalone .py file'

