def inverse(s) :
    if len(s) == 1 :
        return s
    else : 
        a = s[-1]
        s = s[:len(s)-1]
        return a + inverse(s)
print(inverse("Hellofgdsrew"))