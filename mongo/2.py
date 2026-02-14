from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
my_db = client.get_database("my_db")
school = my_db.get_collection("school")

def list_all(mongo_collection):
    return list(mongo_collection.find())

def insert_school(mongo_collection, **kargs):
    return mongo_collection.insert_one(kargs).inserted_id

school_collection = school

id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
print(list_all(school))