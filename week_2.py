"""
Task 2.1 - Some Math 
1. Create a Python program that reads in two numeric values from user 
2. Include a checking mechanism to ensure both values are numeric positive numbers 
3. Perform addition, subtraction, Multiplication and division.
4. Print out the result 
5. Test run the program and check if it tallies with your own calculation
"""



num_1 = float(input("Enter the first number here:"))
num_2 = float(input("Enter the second number here:"))

while num_1 < 0:
    num_1 = float(input("Enter the first number here:"))
while num_2 < 0:
    num_2 = float(input("Enter the second number here:"))

print(f"""
The computation results are: 
{num_1} + {num_2} = {num_1+num_2}
{num_1} - {num_2} = {num_1-num_2} 
{num_1} * {num_2} = {num_1*num_2}
{num_1} / {num_2} = {num_1/num_2}
""")


"""
Task 2.1 Some Math (Extension)
Continue from the previous task, add in try-except block to reject non-numeric values
"""
try:
    num_1 = float(input("Enter the first number here:"))
    num_2 = float(input("Enter the second number here:"))
except ValueError:
    print("Please input numeric values only")
    num_1 = float(input("Enter the first number here:"))
    num_2 = float(input("Enter the second number here:"))

while num_1 < 0:
    num_1 = int(input("Enter the first number here:"))
while num_2 < 0:
    num_2 = int(input("Enter the second number here:"))

print(f"""
The computation results are: 
{num_1} + {num_2} = {num_1+num_2}
{num_1} - {num_2} = {num_1-num_2} 
{num_1} * {num_2} = {num_1*num_2}
{num_1} / {num_2} = {num_1/num_2}
""")



"""
Task 2.2 - Correcting Errors in the code
NAME = input("What is your name?")
to_continue = input("Do you want to play y/n?")
if to_continue = y:
play = input("What to play?\n [C] Chess \n [P] Pokemon")
if play == p
print("Let's go and catch poke.")
else if play == c
print("I'll play chess with you")
else
print("Good bye")
"""

name = input("What is your name?")
to_continue = input("Do you want to play? (y/n)")

if to_continue == "y":
    play = input("What do you want to play?\n [C] Chess \n [P] Pokemon\n")
    if play == "c":
        print("lets play some chess")
    elif play == "p":
        print("Lets go catch some pokemon")
    else:
        print("Goodbye")
        
        
"""
Task 2.3 Forex Converter 2 
Create a Python program with the following specifications:
– Print out a forex menu with appropriate wordings.
– SGD exchange rates are listed below:
SGD to USD: 0.73829
SGD to MYR: 3.05657
SGD to EUR: 0.66323
SGD to GBP : 0.55172
SGD to AUD: 1.07305
– Print out menu options to indicate the available currencies.
– Ask user for the currency to exchange to and the amount to convert.
– The money changer makes a profit of 1% on every transaction. If the amount of value is more than SGD$5000, a discount of 0.5% is given to
customer.
– Display the output showing the converted values.
"""

menu = """
SGD exchange rates are listed below:
SGD to USD: 0.73829
SGD to MYR: 3.05657
SGD to EUR: 0.66323
SGD to GBP : 0.55172
SGD to AUD: 1.07305
"""

sgdusd = 0.73829
sgdmyr = 3.05657
sgdeur = 0.66323
sgdgbp = 0.55172    
sgdaud = 1.07305

print(menu)
currency = input("Enter the currency to exchange (eg USD/MYR/EUR):")
amount = float(input("Enter the amount to exchange here:"))

if amount <= 5000: 
    if currency == "USD":
        print(f"The equivalent amount in {currency} is ${0.99*amount*sgdusd}")
    elif currency == "MYR":
        print(f"The equivalent amount in {currency} is ${0.99*amount*sgdmyr}")
    elif currency == "EUR":
        print(f"The equivalent amount in {currency} is ${0.99*amount*sgdeur}")
    elif currency == "GBP":
        print(f"The equivalent amount in {currency} is ${0.99*amount*sgdgbp}")
    elif currency == "AUD":
        print(f"The equivalent amount in {currency} is ${0.99*amount*sgdaud}")
    else:
        print("Please enter a valid currency")
elif amount > 5000:
    if currency == "USD":
        print(f"The equivalent amount in {currency} is ${0.995*amount*sgdusd}")
    elif currency == "MYR":
        print(f"The equivalent amount in {currency} is ${0.995*amount*sgdmyr}")
    elif currency == "EUR":
        print(f"The equivalent amount in {currency} is ${0.995*amount*sgdeur}")
    elif currency == "GBP":
        print(f"The equivalent amount in {currency} is ${0.995*amount*sgdgbp}")
    elif currency == "AUD":
        print(f"The equivalent amount in {currency} is ${0.995*amount*sgdaud}")
    else:
        print("Please enter a valid currency")



"""
Task 2.4 - Simple Interest
Write a program that asks the user to enter the principal sum that he/she would like to 
invest in an investment opportunity that pays an interest rate of 1% per annum. Print out
the total amount received in the investment using simple interest formula.The printed statement 
should look something like this:
At a yearly interest rate of 1.0 %, you will receive $ 101.0 at the end of 1 years
if you invest $ 100.0 now.

(Hint: Simple interest formula: A = P(1 + rt)
where: A = Total Accrued Amount (principal + interest)
P = Principal Sum
I = Interest Amount
r = Rate of Interest per year in decimal; r = R/100
R = Rate of Interest per year as a percent; R = r * 100
t = Time Period involved in years
"""


investment_amount = float(input("Please enter the principal amount you would like to invest: "))
years = int(input("How many years would you like to invest for? "))

int_rate = 1 
print(f"""
      At a yearly interest rate of {int_rate}%, you will receive 
      ${investment_amount*(1 + (int_rate/100 * years))} if you
      invest  ${investment_amount} now.""")



"""
Task 2.5 - Ratio Analysis 
The code contains some Errors. 
1. Fix the errors by modifying the code 
2. Fix the errors using exception

current_asset = 600000
current_liability = "46000"
current_ratio = current_asset / current_liability
net_income = 1200000
total_share = 6150000
eps = net_income / total_share
print("The current ratio is ", current_ratio)
print("The EPS is ", eps)
"""

current_asset = 600000
current_liability = 46000
current_ratio = current_asset/current_liability

net_income = 1200000
total_share = 6150000
eps = net_income/total_share

print("The current ratio is ", current_ratio)
print("The EPS is ", eps)











