'''
Developer: Ömer ULUTÜRK
Date: 15.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
'''
from functools import reduce
def perfect_number(n):
    # To store sum of divisors 
    sum = 0
    # Find all divisors and add them 
    for x in range(1, n):
        if n % x == 0:
            sum += x
    # If sum of divisors is equal to n, then n is a perfect number 
    return sum == n
    
# Driver program 
n = 2
l=list()
for n in range (1000): 
    if perfect_number (n):
        l.append(n)
print("Sum of all perfect numbers till 1000 is: ", reduce(lambda x,y : x+y, l)) 
