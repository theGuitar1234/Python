def permutation(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]

    result = []
    for i in range(len(list)):
        current = list[i]
        remaining = list[:i] + list[i+1:]
        for j in permutation(remaining):
            result.append([current] + j)

    return result

list = [1, 2, 3]
permutations_list = permutation(list)

for i in permutations_list:
    print(i)
