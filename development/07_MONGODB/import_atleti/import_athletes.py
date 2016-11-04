# This is just a simple mongo Connector used to
# Fill a db "olimpiadi" with a collection named "atleti"
# that contains all the atlethes from the CSV source file.

# To run this script you can simply run from a terminal:
# python import_athletes.py athletes_sochi.csv

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client.olimpiadi

# DATA FORMAT
# age,birthdate,gender,height,name,weight,
# gold_medals,silver_medals,bronze_medals,
# total_medals,sport,country

with open('athletes_sochi.csv', 'r') as file:
    for line in file.readlines():
        splitted = line.split(',')
        if splitted[0] != 'age':
            data = {'age':splitted[0],
                'birthdate':splitted[1],
                'gender':splitted[2],
                'height':splitted[3],
                'name':splitted[4],
                'weight':splitted[5],
                'gold_medals':int(splitted[6]),
                'silver_medals':int(splitted[7]),
                'bronze_medals':int(splitted[8]),
                'total_medals':int(splitted[9]),
                'sport':splitted[10],
                'country':splitted[11][:-2]}
            db.atleti.insert(data)


# Instead to use the python script we can also use MONGOIMPORT
# provided by MongoDB itself:

# mongoimport --db olimpiadi --collection atleti --file atleti.json

# To export the entire collection we can use MONGOEXPORT:

# mongoexport --db olimpiadi --collection atleti --out atleti.json
