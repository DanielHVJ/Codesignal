## if Statements
#
#

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(f"I have a {car.upper()}")
    else:
        print(car.title()) 

## Checking for Inequality

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!") ## True

## Using and to Check Multiple Conditions

age_0 = 12
age_1 = 45 
age_0 >= 21 and age_1 >= 21 

age_1 = 33
age_0 >= 21 and age_1 >= 21 

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings


banned_users = ['andrew', 'carolina', 'david', 'elsa']
user = 'elsa'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"wait until lines crosses each other again\nremember life is a matrix")

## Boolean Expressions
game_active = True
can_edit = False

## EX 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

car = 'subaru'
if car not in cars:
    print(f"{car.lower()}, you can try Mercedes.")
else:
    print(f"{cars[1].upper()} is a great choice")

try_0 = 12
try_1 = 45 
try_0 <= 81  and try_1 >= 33

try_1 = 40
try_0 >= 60 and try_1 >= 70
time = 30

if try_1 >= 45:
    print('Lets go')
    print('Make a three choice')
elif time >= 90:
    print('Pick up 3 and lets go')
elif try_1 > 12 and try_0 > 45:
     print('Pick up 3 and lets go')   
else:
    print(f"Sorry it's not time yeat {time} days only")

## EX 1

alien = ['r','g', 'y']
col = 'r'

if col in alien:
    print('You earned 5 points')
elif col not in alien:
    print('You earned 10 points')
    
if col == alien[1]:
    print('You earned 5 points, green alien')
elif col == alien[2]:
    print('You earned 10 points, yellow alien')
else:
    print('You earned 15 points, blue alien')

age = 67
if age >= 0 and age < 2:
    print('a baby')
elif age >= 2 and age <= 4:
    print('a toddler')
elif age > 4 and age <=13:
    print('Kid') 
elif age > 13 and age <= 20:
    print('Teenager')    
elif age > 20 and age <= 65:
    print('Adult')
else:
    print('Elder')    

### checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


### Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
 
print("\nFinished making your pizza!")

## EX 2

unames = ['Admin', 'Allan', 'Jane', 'John', 'Bruce']
unames = []
user = 'Dai'

if not unames: # check if list is empty
    print('User names list not found')
elif user == unames[0] :
    print(f"Hello {unames[0]} would you like to see a status report?.")
elif user != unames[0] and user in unames:
    print(f"Hello {user}, thank you for logging in again.")
else:
    print(f" User: {user}, not found.")

new = ['Dani', 'Admin', 'JOHN', 'Luca', 'Boris']
upp_user = []
for i in unames:
    upp_user.append(i.upper())
print(upp_user) 

for u in new:
    if u in unames or u in upp_user:
        print(f"not adding {u}.")
    else:
        print(f"You have created {u} user.")
 
print("\nFinished making user list!")

import numpy as np

ord_num = np.arange(1,9,1)

for o in ord_num:
    if o in ord_num[0:3]:
        print(f"{o}st")
    else:
        print(f"{o}th")
 
print("\nFinished making ordinal number list!")



