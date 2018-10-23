'''
Problem Statement:  (Print distinct numbers) Write a program that reads in numbers separated by a
space in one line and displays distinct numbers (i.e., if a number appears multiple
times, it is displayed only once). (Hint: Read all the numbers and store
them in list1. Create a new list list2. Add a number in list1 to list2.
If the number is already in the list, ignore it.) Here is the sample run of the
program:

Enter ten numbers:
The distinct numbers are: 1 2 3 6 4 5
1 2 3 2 1 6 3 4 5 2
'''

mat = input("Enter ten numbers: ")
list1 = mat.split(" ")
list2 =[]

for each in list1:
    if not each in list2:
        list2.append(each)

print("The distinct numbers are:",' '.join(list2))