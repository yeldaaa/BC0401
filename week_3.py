"""
Task 3.1 - Looping Exercise (While)

Get User to enter a number, use while loop  to do the following:
    1. Print out from the number 1 until the number user entered in ascending order.
    2. Print out from the number the user entered down to 1 in descending order.
    3. Print out the timetable for the number the user entered.  Eg. If user entered 5, 
    your program will output 1 x 5 = 5 … until 10 x 5 = 50.
"""

num = int(input("Enter a number here:"))

i = 1
while i <= num:
    print (i)
    i += 1
j = num 
while j >= 1:
    print (j)
    j -= 1
k = 1 
while k <= 10:
    print(f"{k} X {num} = {k*num}")
    k += 1
    
"""
Task 3.2 – Looping Exercises (For)
Get user to enter a number, use for loop and/or
while loop to do the following:
    1. Print out from number 1 until the number
    user entered in ascending order.
    2. Print out from the number user entered
    down to 1 in descending order.
    3. Print out the time table for the number user
    entered. Eg. If user entered 5, your program
    will output 1 x 5 = 5 … until 10 x 5 = 50.
"""

num_1 = int(input("Enter a number here: "))

for i in range(1,num_1 + 1):
    print(i)

for i in range(num_1, 0, -1):
    print(i)
    
for i in range(1,11):
    print(f"{i} X {num_1} = {i*num_1}")



"""
Task 3.3 – Calculate mean
• Write a Python code to calculate the mean of a list of numbers
entered by users. The program exits when “e” is entered.
– See the running of program on the right side.
– User enters the integers until “e” is entered.
– Code prints the average of all integers entered.
"""

mean = []

while True: 
    num = input("Enter an integer (e to quit):")
    if num != "e":
        mean.append(int(num))
    elif num == "e" and len(mean) > 0:
        print("The mean is: ",(sum(mean)/len(mean)))
        break
    elif num =="e":
        print("Goodbye and thanks for nothing")
        break
    

"""
Task 3.4 - Compound Interest
Complete a program to compute compounding interest. Assuming compounding once a year.
Compound interest is compounded yearly with the folllowing year uses the previous year's
principal plus interest as its principal. For example if the initial principal is
$10,000.00, interest rate is 5%, the interest in year 1 is $500.00, and
interest for year 2 will be$1,025.00. Formula as follows:
 amount = initial principal * (1 + interest rate)^period
"""

interest_rate = float(input("Enter Interest Rate:"))
period = int(input("Enter period:"))
principal = float(input("Enter Principal Amount here:"))
total_interest = 0


for i in (1, period):
    sub_total = principal *((1+ interest_rate/100)** i)
    total_interest += sub_total 
    print(f"Total value for period {i} is {sub_total} ")















