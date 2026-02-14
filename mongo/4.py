from pymongo import MongoClient
import json
from bson import json_util

client = MongoClient("mongodb://localhost:27017/")

my_db = client.get_database("my_db")

def schools_by_topic(mongo_collection, topic):
    return mongo_collection.find(topic)

def list_all(mongo_collection):
    result = {}
    with open("result.json", 'w') as f:
        f.write("[")
        for i in mongo_collection.find():
            json.dump(i, f, indent=4, default=json_util.default)
            f.write(",\n")
        f.seek(f.tell()-3)
        f.write("]")

school = my_db.get_collection("school")

j_schools = [
        { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        { 'name': "UCLA", 'topics': ["C", "Python"]},
        { 'name': "UCSD", 'topics': ["Cassandra"]},
        { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]

def insert_school(mongo_collection, **kargs):
    return mongo_collection.insert_one(kargs)

for i in j_schools:
    for key, value in i.items():
        insert_school(school, key=value)

print(list_all(school))