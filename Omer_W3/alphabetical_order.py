'''
Developer: Ömer ULUTÜRK
Date: 15.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words. 
Example:

Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
'''

def alphabetical_order():
    s = input("Please enter your words with hyphen (-) in between them:   ")
    s = s.split("-")
    print(s)
    return print("-".join(sorted(s, key = lambda x:x.lower())))
alphabetical_order()
