import sys
import pymongo 

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
    print('Connected to MongoDB via PyMongo')
except Exception:
    print("Unable to connect to the server.")


rasaDB = pymongo.MongoClient("mongodb://localhost:27017/")

rasa = rasaDB["rasa"]

print(rasaDB.list_database_names())

dblist = rasaDB.list_database_names()
if "rasa" in dblist:
    print("The database exists.")


rasaDB = pymongo.MongoClient("mongodb://localhost:27017/")
rasa = rasaDB["rasa"]

customers = rasa["customers"]

print(rasa.list_collection_names())

collist = rasa.list_collection_names()
if "customers" in collist:
    print("The collection exists.")
else:
    print("The collection doesn't exists")



testCol = rasa["test"]

mydict = { "name": "John", "address": "Highway 37" }

x = testCol.insert_one(mydict)


