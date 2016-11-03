from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 4
# Utilizzando il dataset, calcolare per ogni eta il numero di atleti.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_04(MRJob):
    def steps(self):
        return []

    def lineMapper(self, _, line):
        pass

    def ageReducer(self, age, occurrences_list):
        pass

if __name__ == '__main__':
    MREx_04.run()
