students = [
    {"name": "Alice", "courses": ["Math", "History"]},
    {"name": "Bob", "courses": ["Math", "Biology"]},
    {"name": "Charlie", "courses": ["History", "Biology"]}
]

unique_courses = set()
for i in students:
    for j in i["courses"]:
        unique_courses.add(j)
print(unique_courses)