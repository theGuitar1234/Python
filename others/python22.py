def sort_by_frequency(lst):
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    
    frequencies = []
    for num in unique_elements:
        count = lst.count(num)
        frequencies.append((num, count))
    
    sorted_elements = sorted(frequencies, key=lambda x: (-x[1], x[0]))
    
    result = []
    for num, freq in sorted_elements:
        result.extend([num] * freq)
    
    return result

lst = [4, 5, 6, 5, 4, 3]
print(sort_by_frequency(lst))
