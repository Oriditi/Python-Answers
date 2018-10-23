'''
Problem Statement:  Write a program that reads a list of scores and then assigns grades
based on the following scheme:
The grade is A if score is best – 10.
The grade is B if score is best – 20.
The grade is C if score is best – 30.
The grade is D if score is best – 40.
The grade is F otherwise.

Enter scores:
Student 0 score is 40 and grade is C
Student 1 score is 55 and grade is B
Student 2 score is 70 and grade is A
Student 3 score is 58 and grade is B
'''


def findGrades(lst):
    best = int(max(lst))
    i = 0
    while i < len(lst):
        score = int(lst[i])
        if score >= best - 10:
            print("Student ", i, " score is ", score, " and grade is A")
        elif score >= best - 20:
            print("Student ", i, " score is ", score, " and grade is B")
        elif score >= best - 30:
            print("Student ", i, " score is ", score, " and grade is C")
        elif score >= best - 40:
            print("Student ", i, " score is ", score, " and grade is D")
        else:
            print("Student ", i, " score is ", score, " and grade is F")
        i += 1
def main():
    scores = (input("Enter scores: "))
    lst = (scores.split())
    findGrades(lst)
main()