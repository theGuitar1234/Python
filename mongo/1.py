from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
my_db = client.get_database("my_db")

#school = my_db.create_collection("school", None, None, None, None, None, True)
#school.insert_one({"name": "Holberton school"})

school = my_db.get_collection("school")
# print(list(school.find()))

def list_all(mongo_collection):
    return list(mongo_collection.find())
print(list_all(school))