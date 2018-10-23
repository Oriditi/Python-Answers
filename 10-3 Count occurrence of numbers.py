'''
Problem Statement:  (Count occurrence of numbers) Write a program that reads some integers
between 1 and 100 and counts the occurrences of each. Here is a sample run of
the program:

Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2
2 occurs 2 times
3 occurs 1 time
4 occurs 1 time
5 occurs 2 times
6 occurs 1 time
23 occurs 1 time
43 occurs 1 time
'''

def main():
    numberString = input("Enter integers between 1 and 100: ")
    counts = [0 for i in range(1, 101)] #100 integers...
    numsLst = numberString.split(" ") #split up the input
    nums = [int(x) for x in numsLst] #numbers

    for num in nums:
        counts[num - 1] += 1 #add to counts

    for i in range(len(counts)):
        if counts[i] != 0:
            print (str(i + 1) + " occurs " + str(counts[i]) + " times")
main()