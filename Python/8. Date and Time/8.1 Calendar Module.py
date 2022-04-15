# Problem: https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2022))
date = list(map(int, input().split(' ')))
print(calendar.day_name[calendar.weekday(date[2], date[0], date[1])].upper())