from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 7
# Calcolare per ogni nazione il numero di medaglie, rispettivamente per oro, argento e bronzo.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_07(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.lineMapper,
                   reducer=self.ageReducer),
            MRStep(mapper=self.maxMedal_mapper,
                   reducer=self.maxMedal_reducer)
        ]

    def lineMapper(self, _, line):
        country= line.split(',')[11]
        gold_medal = line.split(',')[6]
        silver_medal = line.split(',')[7]
        bronze_medal = line.split(',')[8]
        #gender = line.split(',')[2]
        try:
            yield country, (('gold_medal', int(gold_medal)), ('silver_medal',int(silver_medal)), ('bronze_medal',int(bronze_medal)))
        except:
            pass

    def ageReducer(self, country, occurrences_list):
        #yield country, sum(occurrences_list[0][1]) 
        total_gold = 0
        total_silver = 0
        total_bronze = 0
        for x in occurrences_list:
            #print x[0][1]
            #if(x[0][0]=='gold_medal'):
            total_gold = total_gold + x[0][1]
            total_silver = total_silver + x[1][1]
            total_bronze = total_bronze + x[2][1]
        yield country, (total_gold+total_silver+total_bronze, total_gold, total_silver, total_bronze)
        
    def maxMedal_mapper(self, country, medals):
        yield "TOTAL", (medals,country)
    
    def maxMedal_reducer(self,_,country_medals):
        #for x in country_medals:
        #    print x
        yield "TOTAL", max(country_medals)
        
if __name__ == '__main__':
    MREx_07.run()
