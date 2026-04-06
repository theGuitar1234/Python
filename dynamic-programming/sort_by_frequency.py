def sort_by_frequency(z):
    unique_elements = []
    for i in z:
        if i not in unique_elements:
            unique_elements.append(i)
    
    frequencies = []
    for j in unique_elements:
        count = z.count(j)
        frequencies.append((j, count))
    
    n = len(frequencies)
    for i in range(n):
        for j in range(0, n - i - 1):
            if frequencies[j][1] < frequencies[j + 1][1] or (frequencies[j][1] == frequencies[j + 1][1] and frequencies[j][0] > frequencies[j + 1][0]):
                frequencies[j], frequencies[j + 1] = frequencies[j + 1], frequencies[j]

    result = []
    for i in frequencies:
        for j in range(i[1]) :
            result.append(i[0])
    
    return result

z = [4, 5, 6, 5, 4, 3]
print(sort_by_frequency(z))
