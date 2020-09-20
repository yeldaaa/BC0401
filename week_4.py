"""
Task 4.1
Write a Python function countVowels(s) that
takes a string value and prints out how many
vowels the string s contains.
– Eg, s=“a quick fox”
countVowels(s)  will output 4
– Eg, s=“a quick brown fox”
countVowels(s)  will output 5
"""

def countVowels(s):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in s.lower():
        if letter in vowels:
            count += 1
    print (count)
    
        
"""
Task 4.2 
Write a Python Function hypotenuse() to ask user to input the lengths of a triangle 
and store it in variables a and b. The function then calculates and prints out the 
longer side of a right angle triangle according to the given lengths a and b.
– Eg, if a = 3, b=4,  5
– Eg, if a=10, b=12,  15.6205
• You can make use of sqrt() function from math
library
"""
import math

def hypotenuse(a, b):
    long_side = math.sqrt(a**2 + b**2)
    print("The hypotenuse of the triangle is: ", long_side)
    
    
"""
Task 4.3
Write (define) a function that gets a valid positive number within the
given range from user. The function takes in 3 inputs parameters from
caller, first input is the minimum, second input is the maximum and third
input indicates the name of data associated with user input. Use a while
loop to continue getting user input if the value is invalid. The function
should do the necessary checking including valid number within the min
and max range. Example of calling the function: get_number(10, 1000,
“principal”), it should then return a valid number between 0 and 100
(inclusive of 0 and 100) back to caller. Decimal number is possible. The
third input argument is used in message prompt to indicate to user the
type of number this function is getting.
"""
    

def get_number(min, max, datatype):
    while max > min:
        entry = float(input(f"Enter a value for {datatype} between {min} and {max}:"))
        if entry>= min and entry <=max:
            print(f"Value of {entry} accepted.")
            return entry
            break
        else:
            print("Invalid input please try again")
            break  




"""
Task 4.4 
Write a main function with appropriate message. Within
your main(), make use of the function you have previously
written in Task 3.3 to get 3 numbers (by calling the function
thrice): period, interest rate and principal amount. Store the
return values in appropriate variables and decide on the
appropriate number range for each number. Compute
simple interest using the formula:
Total amount = principal * (1 + interest rate * period)
"""


def main():
    period = float(get_number(5, 10, "period"))
    interest = float(get_number(0.01, 0.05, "interest"))
    principal = float(get_number(10, 100000, "principal"))
    total_interest = principal * (1+interest)**period - principal
    print(f"The total interest is:{total_interest}")

