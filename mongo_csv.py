import csv
import json
import pandas as pd
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient()

# Connect to the test db 
db=client.station

# Use the employee collection
station = db.station


df=pd.read_csv("clean.csv")
df = df.rename({'Unnamed: 0.1':'ID','Unnamed: 0': 'Read ID'}, axis=1)

df=df.set_index('ID')

df=df.head(10)

df.to_csv('out.csv')

def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['ID']
            data[key] = rows
            
         
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        
       
        


    

make_json('out.csv','nosql.json')


with open('nosql.json') as f:
    file_data = json.load(f)
    station.insert_one(file_data)

# # Query for the inserted document.
# Queryresult = station.find_one({'Read ID': '1'})
# print(Queryresult)

