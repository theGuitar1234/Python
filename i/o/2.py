def write_file(path, content):
    with open(path, 'w', encoding="utf-8") as f:
        return f.write(content)
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
