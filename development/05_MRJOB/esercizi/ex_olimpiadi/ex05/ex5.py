from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 5
# Partendo dall'esercizio precedente, restituire come output l'eta' con il numero maggiore di occorrenze.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_05(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.lineMapper,
                   reducer=self.ageReducer),
            MRStep(mapper=self.mapper_findmax,
                   reducer=self.reducer_findmax)
            ]

    def lineMapper(self, _, line):
        age= line.split(',')[0]
        if age!='age':
                yield age, 1

    def ageReducer(self, age, occurrences_list):
        yield age, sum(occurrences_list)
    
    def mapper_findmax(self, age, occurences):
        yield 'max', [occurences, age]
    
    def reducer_findmax(self, key, freqs):
        #print key
        #for x in freqs:
        #    print x
        yield "MAX", max(freqs)

if __name__ == '__main__':
    MREx_05.run()
