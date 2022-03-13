# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    num_sub = int(len(string)/k)
    for sub_num in range(num_sub):
        sub = string[sub_num*k:sub_num*k+k]
        sub_list, unique_sub_list = list(sub), []
        [unique_sub_list.append(letter) for letter in sub_list if letter not in unique_sub_list]
        # cannot use set since order of unique_sub_list matters
        # unique_sub_list = list(set(sub_list))
        unique_sub = ''.join(unique_sub_list)
        print(unique_sub)

string, k = input('Enter string: '), int(input('Enter k: '))
merge_the_tools(string, k)