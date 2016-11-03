from mrjob.job import MRJob
from mrjob.step import MRStep

import re

WORD_REGEXP = re.compile(r"[\w']+")

# Exercise 4
# Utilizzando il dataset, calcolare per ogni eta il numero di atleti.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_04(MRJob):
    def steps(self):
        return [
                MRStep(mapper=self.lineMapper,
                       reducer=self.ageReducer)
            ]
        

    def lineMapper(self, _, line):
        # print line
        age= line.split(',')[0]
            
        # atleta = WORD_REGEXP.findall(line)
        # print atleta
        if age!='age':
        #print words[0]
            yield age, 1
            
        #leggere il file

    def ageReducer(self, age, occurrences_list):
            #print age
            #for r in occurrences_list :
            #    print r
            yield age, sum(occurrences_list)  

if __name__ == '__main__':
    MREx_04.run()
