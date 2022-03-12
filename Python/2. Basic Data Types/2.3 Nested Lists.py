# Problem: https://www.hackerrank.com/challenges/nested-list/problem

records, sorted_scores = [], []
while True:
    for _ in range(int(input('Enter total number of students: '))):
        name = str(input('Enter name of student: ')).title()
        score = float(input("Enter the student's score: "))
        record = [name, score]
        records.append(record)
        print("Enter next student's details...")
    sorted_scores = sorted(list(set([record[1] for record in records])))
    if len(sorted_scores) <= 1:
        try_again = str(input('You have submitted 1 or less unique score. Would you like to try again? (Y/N)')).upper()
        if try_again == 'N':
            break
        else: continue

    second_lowest_grade = sorted_scores[1]
    print(*sorted([record[0] for record in records if second_lowest_grade in record]), sep='\n')
    break