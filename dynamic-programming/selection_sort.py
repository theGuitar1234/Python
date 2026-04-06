def selection_sort(z):
    for i in range(len(z)):
        min_index = i
        for j in range(i + 1, len(z)):
            if z[j] < z[min_index]:
                min_index = j
        z[i], z[min_index] = z[min_index], z[i]
        print(z) 
    return f"\nSorted list: {z}"

z = [1, 4, 3, 6, 8, 0]
print(selection_sort(z))
