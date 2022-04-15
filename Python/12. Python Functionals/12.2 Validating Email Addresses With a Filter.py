# Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re
def fun(s):
    # return True if s is a valid email, else return False
    try:
        username = s.split('@')[0]
        website = s.split('@')[1].split('.')[0]
        extension = s.split('@')[1].split('.')[1]
        if (len(username) > 0) and (len(website) > 0) and (len(extension) > 0) and \
            re.match("^[A-Za-z0-9_-]*$", username) and \
            re.match("^[A-Za-z0-9]*$", website) and \
            re.match("^[A-Za-z]*$", extension) and (len(extension) <= 3):
            return True
        else: return False
    except:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))


n = int(input())
emails = []
for _ in range(n):
    emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)