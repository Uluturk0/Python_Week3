'''
Developer: Ömer ULUTÜRK
Date: 15.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a function that outputs the transcription of an input number with two digits.
Example:

28---------------->Twenty Eight
'''

def reading_number(n):
    numbers = "zero one two three four five six seven eight nine".split()
    numbers.extend("ten eleven twelve thirteen fourteen fifteen sixteen".split())
    numbers.extend("seventeen eighteen nineteen".split())
    numbers.extend(tens if ones == "zero" else (tens + "-" + ones) 
        for tens in "twenty thirty forty fifty sixty seventy eighty ninety".split()
        for ones in numbers[0:10])
    print(n, "---------------->", numbers[n])
n=int(input("Enter a number range in 0-99:"))
reading_number(n)