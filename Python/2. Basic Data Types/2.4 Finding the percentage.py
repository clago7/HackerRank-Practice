# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
tot_score = 0
for score in student_marks[query_name]:
    tot_score += score
avg_score = tot_score/(len(student_marks[query_name]))
print(f'{avg_score:,.2f}')