from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 4
# Utilizzando il dataset, calcolare per ogni eta il numero di atleti.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_04(MRJob):
    def steps(self):
        return [MRStep(mapper=self.lineMapper,
                       reducer=self.ageReducer)]

    def lineMapper(self, _, line):
        splitted = line.split(',')
        if splitted[0] == 'age': return
        yield splitted[0], 1

    def ageReducer(self, age, occurrences_list):
        yield age, sum(occurrences_list)



if __name__ == '__main__':
    MREx_04.run()
