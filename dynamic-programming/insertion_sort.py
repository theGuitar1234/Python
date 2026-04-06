def insertion_sort(z) :
    for i in range(1, len(z)) :
        key = z[i]
        j = i-1
        while j>=0 and z[j] > key :
            z[j+1], z[j] = z[j], z[j+1]
            print(z)
            j=j-1
        z[j+1] = key
    return f"\n {z}"
z = [1, 4, 3, 6, 8, 0]
print(insertion_sort(z))