from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 6
# Calcolare il numero di uomini e donne per ogni eta.
# Successivamente calcolare per donne e uomini il MAX e il MIN delle occorrenze.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_06(MRJob):
    def steps(self):
        return [MRStep(mapper=self.lineMapper,
                       reducer=self.ageReducer),
                MRStep(mapper=self.order_by_occurrences,
                       reducer=self.return_max)]

    def lineMapper(self, _, line):
        splitted = line.split(',')
        if splitted[0] == 'age': return
        yield (splitted[0], splitted[2]), 1

    def ageReducer(self, age_gender, occurrences_list):
        yield age_gender, sum(occurrences_list)

    def order_by_occurrences(self, age_gender, occurrences):
        if age_gender[1] == "Male":
            yield "MAN_MAX", (occurrences, age_gender[0])
            yield "MAN_MIN", (occurrences, age_gender[0])
        else:
            yield "FEMALE_MAX", (occurrences, age_gender[0])
            yield "FEMALE_MIN", (occurrences, age_gender[0])

    def return_max(self, key, values):
        if key[-3:] == "MAX":
            yield key, max(values)
        else:
            yield key, min(values)


if __name__ == '__main__':
    MREx_06.run()
