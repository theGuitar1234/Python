a = "pwwkew"

max = 0

dict = {}
set = set()

for i in range(len(a)) :
    if (a[i] in set) :
        dict[a[i]] = i
    set.add(a[i])
print(dict, set)

for i in range(len(dict.keys())) :
    for j in range(i, len(dict.keys())) :
        left = i
        right = j 
        print(a[left:right])

# left = 0
# right = len(a)-1

# leftSet = set()
# rightSet = set()

# while (right >= 0) :
#     print(a[left])
#     if (a[left] in leftSet) :
#         leftSet.clear()
#     leftSet.add(a[left])
#     print(leftSet)
#     if (len(leftSet) > max) :
#         max = len(leftSet)
    
#     print(a[right])
#     if (a[right] in rightSet) :
#         rightSet.clear()
#     rightSet.add(a[right])

#     print(rightSet)
#     if (len(rightSet) > max) :
#         max = len(rightSet)
    
#     left += 1
#     right -= 1

# l = 0
# r = len(a) - 1

# while (r > l) :
#     if (len("".join(set(a[l:r+1]))) == len(a[l:r+1])) :
#         if (len(a[l:r+1]) > max) :
#             max = len(a[l:r+1])
#     l += 1
#     r -= 1

# print(max)

# for i in range (b):
#     c += 1
#     if i+1 != b:
#         if a[i] == a[i+1]:
#             z = len(set(a[b-c:b-1]))
#             d.append(z)
#             c = 0
#             continue
#         else:
#             pass
#     else:
#         z = len(set(a[b-c:b-1]))
#         d.append(z)
#         break
# print(max(d))
