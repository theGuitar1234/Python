import json 
import sys
import os

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        values = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in dir(self):
                values[i] = getattr(self, i)
        return values
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)    

def load_from_json_file(filename):
    with open(filename, 'r+') as f:
        return json.load(f)

def read_file(path):
    with open(path, 'r', encoding="utf-8") as f:
        print(f.read())

#path = sys.argv[0]
path = "i/o/example.json"

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

# Initial student:
# <11-student.Student object at 0x7f832826eda0>
# <class '11-student.Student'>
# <class 'dict'>
# John Doe 23
# {"last_name": "Doe", "first_name": "John", "age": 23}
# Saved to disk
# Fake student:
# <11-student.Student object at 0x7f832826edd8>
# <class '11-student.Student'>
# Fake Fake 89
# Load dictionary from file:
# <11-student.Student object at 0x7f832826edd8>
# <class '11-student.Student'>
# John Doe 23