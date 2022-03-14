# Problem: https://www.hackerrank.com/challenges/no-idea/problem

# def happiness_calc(array, set_A, set_B):
#     array_l, A_l, B_l, happiness = list(map(int, array.split(' '))), list(set_A), list(set_B), 0
#     for integer in array_l:
#         if integer in A_l:
#             happiness += 1
#         elif integer in B_l:
#             happiness -= 1
#     return print(happiness)

# n_m_list = [int(integer) for integer in input('Enter number of integers in the array and in sets A/B: ').split(' ')]
# alternatively...use map instead of list comprehension
n_m_list = list(map(int, input('Enter number of integers in the array and in sets A/B: ').split(' ')))
n, m = n_m_list[0], n_m_list[1]
array = list(map(int, input('Enter integers of the array: ').split(' ')))
like, dislike = set(list(map(int, input('Enter integers in set A: ').split(' ')))), set(list(map(int, input('Enter integers in set B: ').split(' '))))
# happiness_calc(array, like, dislike)

# alternatively...since above code is not optimised and will exceed time limit
print(sum((i in like) - (i in dislike) for i in array))