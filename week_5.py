"""
Task 5.1 String Warm-Up Practice
attraction = “Singapore Zoo”
visitors = 1600000
mins_spent = 210
Try to make a sentence in Python using the above variables: (String formatting)
Singapore Zoo attracts 1600000 visitors last year who spent on average 210
mins there.
How about displaying just the last 3 characters from attraction? (String slicing)
Zoo attracts 1600000 visitors last year who spent on average 210 mins there.
Now, try this: (String formatting)
Singapore Zoo attracts 1,600,000 visitors last year who spent on average 3hr
30 mins there.
"""

attraction = "Singapore Zoo"
visitors = 1600000
mins_spent = 210

### String Formatting
print("{} attracts {} visitors last year who spent on average {} mins there".format(attraction, visitors, mins_spent))

print(f"{attraction} attracts {visitors} visitors last year who spent on average {mins_spent} mins there")


### String Slicing
print("{} attracts {} visitors last year who spent on average {} mins there".format(attraction[-3:], visitors, mins_spent))

print(f"{attraction[-3:]} attracts {visitors} visitors last year who spent on average {mins_spent} mins there")


### String Formatting 
print("{} attracts {:,} visitors last year who spent on average {} hr {} mins there".format(attraction, visitors, mins_spent//60, mins_spent%60))


"""
Task 5.2 List Warm-Up Practice
attraction1 = "Singapore Zoo"
attraction2 = "Gardens by the Bay"
attractions = _____ # create an empty list
attractions.append(attraction1)
attractions.append(___________) # add in the second attraction
print(__________) # print out the whole list
print(attractions[__]) # print out the first attraction
"""

attraction1 = "Singapore Zoo"
attraction2 = "Gardens by the Bay"

attractions = []
attractions.append(attraction1) 
attractions.append(attraction2)
print(attractions)
print(attractions[0])


"""
Task 5.3 Dictionary Warm-Up Practice
sales_latte = [10000, 12000, 14000, 34000, 12000, 14000]
sales_muffin = [3000, 2000, 4000, 6000, 2000, 5000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
cafe_dict = ____ # create an empty dictionary
cafe_dict['latte'] = sales_latte # Insert sales of latte into the dictionary
cafe_dict[‘muffin’] = ___________ # Insert sales of muffin into the dictionary
cafe_dict[_______] = ____________ # Insert months into the same dictionary
print(______) # print out the content of dictionary
for each in _____(len(sales_latte)): # loop through the index number of sales_latte list
print("In {}, Latte fetches {} while muffins fetches {}.".format(
____________ , cafe_dict['latte'][each], ____________))
"""

sales_latte = [10000, 12000, 14000, 34000, 12000, 14000]
sales_muffin = [3000, 2000, 4000, 6000, 2000, 5000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

cafe_dict = {}
cafe_dict['latte'] = sales_latte #Insert sales of latte into the dictionary
cafe_dict['muffin'] = sales_muffin
cafe_dict['months'] = months
print(cafe_dict)

for each in range(len(sales_latte)):
    print("In {}, Latte fetches {} while muffins fetches {}".format(cafe_dict['months'][each], cafe_dict['latte'][each], cafe_dict['muffin'][each]))
    
    
    
    
"""
Task 5.4 – String Practice
Write a program that gets a sentence from user and
performs the following:
i. Count the number of upper case in the sentence
ii. Count the number of lower case in the sentence
iii. Print out the characters at odd index number
iv. Split the sentence into words and store it in a list and print
out.
"""

sentence = input("Enter a sentence: ")
uppercount = 0
lowercount = 0 
for i in sentence: 
    if i.isupper():
        uppercount += 1
    elif i.islower():
        lowercount += 1
odd_index = ""
results = f"""
The total upper case is: {uppercount}
The total lower case is: {lowercount}
The odd index characters are: {sentence[::2]}
Converted to list: {sentence.split()}
"""
print(results)


"""
Task 5.5 – List Practice
The above data contains the sales of Lattes and muffins in certain months. It is
arranged in associative list format where the index number from the list
corresponds to another list. For example in Jan, the sales of latte is 10000 and
muffin is 3000. Write codes to answer the following:
i. The highest sales for Latte.
ii. The highest sales for muffin.
iii. The corresponding month(s) with the highest sales for both products.
iv. A new set of data is given. In the month of July, the sales of Latte is 40000
and muffin is 6500. Add these data into the lists and print out
"""


sales_latte = [10000, 12000, 14000, 34000, 12000, 14000]
sales_muffin = [3000, 2000, 4000, 6000, 2000, 5000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

print(max(sales_latte))
print(max(sales_muffin))

sales = dict()
sales['latte']= sales_latte
sales['muffin'] = sales_muffin
sales['months'] = months

index_latte = sales_latte.index(max(sales_latte))
print(f"The month with the highest latte sales is {months[index_latte]}")

index_muffin = sales_muffin.index(max(sales_muffin))
print(f"The month with the highest muffin sales is {months[index_muffin]}")

sales_latte.append(40000)
sales_muffin.append(6500)
months.append("Jul")
print(sales_latte)
print(sales_muffin)
print(months)











    