import sys
import pymongo 
from datetime import datetime
from bson.objectid import ObjectId



# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    # print(client.server_info())
    print('Connected to MongoDB via PyMongo')
except Exception:
    print("Unable to connect to the server.")


# rasaDB = pymongo.MongoClient("mongodb://localhost:27017/")

# rasa = rasaDB["rasa"]

# print(rasaDB.list_database_names())

# dblist = rasaDB.list_database_names()
# if "rasa" in dblist:
#     print("The database exists.")


# rasaDB = pymongo.MongoClient("mongodb://localhost:27017/")
# rasa = rasaDB["rasa"]

# customers = rasa["customers"]

# print(rasa.list_collection_names())

# collist = rasa.list_collection_names()
# if "customers" in collist:
#     print("The collection exists.")
# else:
#     print("The collection doesn't exists")



# testCol = rasa["test"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = testCol.insert_one(mydict)

mentalBotDB = pymongo.MongoClient("mongodb://localhost:27017/")
mentalBot = mentalBotDB["mentalBotDB"]

remindersCollection = mentalBot["reminders"]

# entities = [{"entity": "activity",
# "start":  5,
# "end": 6,
# "confidence_entity": 0.6445619463920593,
# "value": "đập đồ",
# "extractor": "DIETClassifier"}]

# mydict = { "userId": "6258e2b0ee1e676f8626d4bd", "username": "LhMinh2607", "reminder": entities, "createdAt": datetime.today()}

# remindersCollection.insert_one(mydict)

# for obj in remindersCollection.find().sort([('createdAt', -1)]):
#     if obj['userId'] == "6258e2b0ee1e676f8626d4bd":
#         # activity = next(tracker.get_slot("activity"), None)
#         activity = obj["reminder"][0]["value"]
#         print(activity)
#         break
        

usersCollection = mentalBot["users"]

user = usersCollection.find_one({"_id": ObjectId("6258e2b0ee1e676f8626d4bd")})

print("Tên đầy đủ của bạn là "+user['name'])
print("Username của bạn là "+user['username'])
print("Nghề nghiệp của bạn là "+user['occupation'])
print("Số điện thoại của bạn là "+user['phoneNumber'])
print("Email của bạn là "+user['email'])
print("Ngày tháng năm sinh của bạn là "+str(user['dob'])[:10])
print("Tâm trạng hiện tại của bạn do bạn cung cấp là đang "+user['mood'])
print("Tiến độ của bạn là "+user['progress'])
print(user["username"]+" có thể thay đổi thông tin trên trang cá nhân của bạn bất cứ lúc nào")


# print(user['username'])

## reminder is an array
# for obj in remindersCollection.find().sort([('createdAt', -1)]):
#     if obj['userId'] == "6258e2b0ee1e676f8626d4bd":
#         # activity = next(tracker.get_slot("activity"), None)
#         for act in obj["reminder"]:
#             activity = act["value"]
#             print(activity)
#         break

# timer = '1h20m30s'
# splitTimerHour = timer.split('h')
# splitTimerMinute = splitTimerHour[1].split('m')
# splitTimerSecond = splitTimerMinute[1].split('s')
# print(splitTimerHour)
# print(splitTimerMinute)
# print(splitTimerSecond)

# hours = timer.replace('h', '').replace('m', '')  
# print(hours)

# usersCollection = mentalBot['users']

# usersCollection.find_one_and_update({'_id': ObjectId('6258e2b0ee1e676f8626d4bd')}, update={"$set": {'mood': "vui quá trời quá đất"}})

# for obj in usersCollection.find().sort([('createdAt', -1)]):
#     if obj['_id'] == ObjectId("6258e2b0ee1e676f8626d4bd"):
#         print(obj["mood"])
#         break


# reminder is an object
# for obj in remindersCollection.find().sort([('createdAt', -1)]):
#     if obj['userId'] == "6258e2b0ee1e676f8626d4bd":
#         # activity = next(tracker.get_slot("activity"), None)
#         activity = obj["reminder"]["value"]
#         print(activity)
#         break