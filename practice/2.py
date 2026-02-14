data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob"},
        {"name": "Charlie", "age": 30}
    ]
}

for i in data["users"]:
    try:
        print(i["age"])
    except KeyError:
        print("Unknown")