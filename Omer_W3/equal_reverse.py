'''
Developer: Ömer ULUTÜRK
Date: 15.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False
'''

def equal_reverse(s1):
    
    s2="".join(list(reversed(s1)))
    if s1==s2:
        return True
    else:
        return False
print(equal_reverse("ali"))