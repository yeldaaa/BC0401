"""
Task 1.1 
1. Create a Python Program that read in two numeric values from user.
2. Store the values into two variables with meaningful names 
3. Multiply the two values using the two variables. 
4. Print out the result after multiplication.
5. Test run the program and check if it tallies with your own calculation
"""

### Get User input
input_1 =int(input("Enter the First Number:"))
input_2 = int(input("Enter the Second Number:"))

# Multiply the two variables together
result = input_1*input_2

### Print out the result after the multiplication
print( f"The result after multiplication is {result}")


"""
Task 1.2 
Create a Python Program with the following specs:
 – Print out a forex menu with appropriate
wordings.
– Display the exchange rates below to user: 
SGD to USD: 0.73829
SGD to MYR: 3.05657
SGD to EUR: 0.66323
SGD to GBP : 0.55172
SGD to AUD: 1.07305
– Get the value to convert from user.
– Display the output showing the result to include
all converted values.
"""

menu = """
Welcome to the Forex Calculator
    The rates are as shown below:
    SGD to USD: 0.73829
    SGD to MYR: 3.05657
    SGD to EUR: 0.66323
    SGD to GBP :0.55172
    SGD to AUD: 1.07305
"""
print(menu)

value = float(input("Enter SGD value to convert:"))

usdvalue = value * 0.73829
myrvalue = value * 3.05657
eurvalue = value * 0.66323
gbpvalue = value * 0.55172
audvalue = value * 1.07305

print(f"""
      USD value = {usdvalue}
      MYR value = {myrvalue}
      EUR value = {eurvalue}
      GBP value = {gbpvalue}
      AUD value = {audvalue}
""")





