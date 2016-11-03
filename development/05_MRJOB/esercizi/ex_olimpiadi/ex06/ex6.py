from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 6
# Calcolare il numero di uomini e donne per ogni eta.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_06(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.lineMapper,
                   reducer=self.ageReducer)
            ]

    def lineMapper(self, _, line):
        age= line.split(',')[0]
        gender = line.split(',')[2]
        yield age, (gender, 1)

    def ageReducer(self, age, occurrences_list):
        numMale=0
        numFemale=0
        if age!='age':
            for x in occurrences_list:
                if x[0]=='Male':
                    numMale = numMale+x[1]
                else:
                    numFemale = numFemale+x[1]
            yield age, [numMale, numFemale]

            
            
if __name__ == '__main__':
    MREx_06.run()

    
    

    #def ageReducer(self, age, occurrences_list):
            #print age
            #for r in occurrences_list :
            #    print r
     #       yield age, sum(occurrences_list) 