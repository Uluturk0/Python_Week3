'''
Developer: Ömer ULUTÜRK
Date: 15.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a function that filters all the unique(unrepeated) elements of a given list.

Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output : [1, 2, 3, 4, 5]
'''

def unique_list(mylist):
    myset = set(mylist)
    return print([*myset])
unique_list([1,2,3,3,3,3,4,5,5])