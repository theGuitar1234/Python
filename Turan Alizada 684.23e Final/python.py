def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"] # I included the vowels of English letters but you can also add other languages'
    count = 0
    for i in string:
        if i.lower() in vowels:
            count += 1
    return count

print(count_vowels("Turan"))
