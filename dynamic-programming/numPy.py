import numpy as np
arr = np.array([[1, 2], [3, 4]])
total_sum = np.sum(arr)           # Sum of all elements: 10
sum_axis0 = np.sum(arr, axis=0)   # Sum along columns: [4, 6]
sum_axis1 = np.sum(arr, axis=1)   # Sum along rows: [3, 7]

mean_all = np.mean(arr)           # Mean of all elements: 2.5
mean_axis0 = np.mean(arr, axis=0) # Mean along columns: [2, 3]
mean_axis1 = np.mean(arr, axis=1) # Mean along rows: [1.5, 3.5]

product_all = np.prod(arr)           # Product of all elements: 24
product_axis0 = np.prod(arr, axis=0) # Product along columns: [3, 8]
product_axis1 = np.prod(arr, axis=1) # Product along rows: [2, 12]

std_all = np.std(arr)             # Standard deviation of all elements: 1.118
std_axis0 = np.std(arr, axis=0)   # Standard deviation along columns: [1, 1]
std_axis1 = np.std(arr, axis=1)   # Standard deviation along rows: [0.5, 0.5]

var_all = np.var(arr)            # Variance of all elements: 1.25
var_axis0 = np.var(arr, axis=0)  # Variance along columns: [1, 1]
var_axis1 = np.var(arr, axis=1)  # Variance along rows: [0.25, 0.25]

min_all = np.min(arr)            # Minimum value of all elements: 1
max_all = np.max(arr)            # Maximum value of all elements: 4
min_axis0 = np.min(arr, axis=0)  # Min along columns: [1, 2]
max_axis1 = np.max(arr, axis=1)  # Max along rows: [2, 4]

cumsum_all = np.cumsum(arr)       # Cumulative sum: [1, 3, 6, 10]
cumprod_all = np.cumprod(arr)     # Cumulative product: [1, 2, 6, 24]

median_all = np.median(arr)        # Median of all elements: 2.5

percentile_50 = np.percentile(arr, 50)  # 50th percentile (median): 2.5

argmin_all = np.argmin(arr)      # Index of the min element: 0
argmax_all = np.argmax(arr)      # Index of the max element: 3

data = np.array([(1, 'Alice', 4.8), (2, 'Bob', 3.7)],
                dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'f4')])
print(data['name'])  # Output: ['Alice' 'Bob']

masked_arr = np.ma.array([1, 2, 3], mask=[0, 1, 0])  # Masks the second element


