from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 7
# Calcolare per ogni nazione il numero di medaglie, rispettivamente per oro, argento e bronzo.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_07(MRJob):
    def steps(self):
        return []

    def lineMapper(self, _, line):
        pass

    def ageReducer(self, age, occurrences_list):
        pass

if __name__ == '__main__':
    MREx_07.run()
