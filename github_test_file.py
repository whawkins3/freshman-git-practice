'''
HackRank Challenge #1

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Input Format
* A single line containing a positive integer, i.e., 3 .

Constraints
* 1 <= n <= 100

Output Format
* Print Weird if the number is weird. Otherwise, print Not Weird.

'''

n = int(input("Enter a number between 1 and 100: ").strip())

if n % 2 == 0 and (2 <= n <= 5  or n > 20):
    print("Not Weird")
else:
    print("Weird")