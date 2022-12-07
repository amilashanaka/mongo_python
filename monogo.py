# Import the python libraries
from pymongo import MongoClient
from pprint import pprint
import json

# Choose the appropriate client
client = MongoClient()

# Connect to the test db 
db=client.station

# Use the employee collection
station = db.station
# station_struct = {
#     'Name': 'Raj Kumar',
#     'Address': 'Sears Streer, NZ',
#     'Age': '42'
# }

# Use the insert method
# result = station.insert_one(station_struct)

with open('nosql.json') as f:
    file_data = json.load(f)
    station.insert_one(file_data)

# Query for the inserted document.
Queryresult = station.find_one({'Read ID': '1'})
print(Queryresult)