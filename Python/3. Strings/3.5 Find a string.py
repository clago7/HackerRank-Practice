# Problem: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    str_len, sub_len, occurences, start = len(string), len(sub_string), 0, 0
    for _ in range(str_len - sub_len +1):
        if string[start:start+sub_len] == sub_string:
            occurences += 1
        start += 1
    return occurences

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)