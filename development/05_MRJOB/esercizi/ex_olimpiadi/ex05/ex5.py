from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 5
# Partendo dall'esercizio precedente, restituire come output l'eta' con il numero maggiore di occorrenze.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_05(MRJob):
    def steps(self):
        return []

    def lineMapper(self, _, line):
        pass

    def ageReducer(self, age, occurrences_list):
        pass

if __name__ == '__main__':
    MREx_05.run()
