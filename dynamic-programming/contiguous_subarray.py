def contiguous_subarray(list) :
    contiguous_subarray = []
    max_prod = 0

    for i in range(len(list)) :
        for j in range(i+1, len(list)+1) :
            contiguous_subarray.append(list[i:j])

    for i in contiguous_subarray:
        prod = 1
        for j in i :
            prod *= j
        if prod>max_prod :
            max_prod = prod

    return max_prod

list = [6, -3, -10, 0, 2]
print(contiguous_subarray(list))