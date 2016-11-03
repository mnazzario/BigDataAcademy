from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 7
# Calcolare per ogni nazione il numero di medaglie totali e per ciascuna tipologia, rispettivamente per oro, argento e bronzo.
# Successivamente stampare in output la nazione con piu medaglie in totale

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_07(MRJob):
    def steps(self):
        return [MRStep(mapper=self.lineMapper, reducer=self.ageReducer),
                MRStep(mapper=self.order_by_total, reducer=self.find_max)]

    def lineMapper(self, _, line):
        splitted_line = line.split(',')
        try:
            yield splitted_line[-1], (int(splitted_line[6]), int(splitted_line[7]), int(splitted_line[8]))
        except Exception as e:
            # Table Header
            pass

    def ageReducer(self, country, medals):
        # print country, medals
        gold = 0
        silver = 0
        bronze = 0
        total = 0
        for medal in medals:
            gold += medal[0]
            silver += medal[1]
            bronze += medal[2]
        yield country, (gold + silver + bronze, gold, silver, bronze)

    def order_by_total(self, country, medals):
        yield "TOTAL", (medals, country)

    def find_max(self, _, country_medals):
        yield "TOTAL", max(country_medals)

if __name__ == '__main__':
    MREx_07.run()
