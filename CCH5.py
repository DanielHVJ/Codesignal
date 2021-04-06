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

if try_1 >= 45:
    print('Lets go')
    print('Make a three choice')
else:
    print("Sorry it's not time yeat")

-- 118
