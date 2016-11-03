from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 5
# Utilizzando il dataset, calcolare per ogni eta il numero di atleti.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_05(MRJob):
    def steps(self):
        return [MRStep(mapper=self.lineMapper,
                       reducer=self.ageReducer),
                MRStep(mapper=self.order_by_occurrences,
                       reducer=self.return_max)]

    def lineMapper(self, _, line):
        splitted = line.split(',')
        if splitted[0] == 'age': return
        yield splitted[0], 1

    def ageReducer(self, age, occurrences_list):
        yield age, sum(occurrences_list)

    def order_by_occurrences(self, age, occurrences):
        yield "MAX", (occurrences, age)
        yield "MIN", (occurrences, age)

    def return_max(self, key, values):
        if key == "MAX":
            yield "MAX", max(values)
        else:
            yield "MIN", min(values)


if __name__ == '__main__':
    MREx_05.run()
