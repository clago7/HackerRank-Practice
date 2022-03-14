# Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_array, sum_distinct_heights = list(set(array)), 0
    for distinct_height in unique_array:
        sum_distinct_heights += distinct_height
    num_distinct_heights = len(unique_array)
    return round(sum_distinct_heights/num_distinct_heights,3)
n = int(input('Enter total number of plants: '))
arr = [int(height) for height in input('Enter the heights of each plant, separated by a space: ').split()]
result = average(arr)
print(result)