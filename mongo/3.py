from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
my_db = client.get_database("my_db")

def update_topics(mongo_collection, name, topics):
    mongo_collection = my_db.get_collection("school")
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

def list_all(mongo_collection):
    return list(mongo_collection.find())

school = my_db.get_collection("school")
update_topics(school, "Holberton school", ["Sys admin", "AI", "Algorithm"])
print(list_all(school))