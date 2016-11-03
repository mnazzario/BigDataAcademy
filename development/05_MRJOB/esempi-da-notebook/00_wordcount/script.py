# Importiamo la classe MrJob
from mrjob.job import MRJob
import re
WORD_REGEXP = re.compile(r"[\w']+")

# Inizializziamo la classe MRWordFreqCount che eredita da MRJob
class MRWordFreqCount(MRJob):
    
    # Dichiariamo il mapper
    def mapper(self, _, line):
        # Nel nostro caso non avremo una chiave ma solo un value, che corrispondera a una riga del testo in input
        words = WORD_REGEXP.findall(line)
        for word in words:
            # Per ogni parola restituiamo la parola in minuscolo e il numero di occorrenze, ovviamente 1
            yield word.lower(), 1 #yeld ritorna il valore ma continua la funzione

    # Dichiariamo il reducer
    def reducer(self, word, counts):
        # Per ogni parola contiamo il numero delle occorrenze
        yield word, sum(counts) #L'output sara' sempre chiave - tab - valore


if __name__ == '__main__':
    try:
        MRWordFreqCount.run()
    except TypeError:
        print 'MrJob cannot work inside iPython Notebook as it is not saved as a standalone .py file'
        


