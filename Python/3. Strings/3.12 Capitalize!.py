# Problem: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    s_list, titled_list = s.split(' '), []
    for word in s_list:
        try:
            if word[0].isalpha():
                if len(word) > 1:
                    titled_list.append(word[0].upper() + word[1:])
                else: titled_list.append(word.upper())
            else: titled_list.append(word)
        except IndexError:
            titled_list.append(word)
    titled_s = ' '.join(titled_list)
    return titled_s

s = input('Enter string: ')
print(solve(s))