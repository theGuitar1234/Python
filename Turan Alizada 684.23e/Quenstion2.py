#Question 2

import time 

def cocktailSort(a):
	n = len(a)
	swapped = True
	start = 0
	end = n-1
	start_time = time.time()
	while (swapped == True):

		swapped = False

		for i in range(start, end):
			if (a[i] > a[i + 1]):
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True

		if (swapped == False):
			break

		swapped = False

		end = end-1

		for i in range(end-1, start-1, -1):
			if (a[i] > a[i + 1]):
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True

		start = start + 1
	end_time = time.time()
	print(end_time-start_time)

a = [5, 1, 4, 2, 8, 0, 2]
cocktailSort(a)
print("Sorted array is:")
for i in range(len(a)):
	print(a[i])


