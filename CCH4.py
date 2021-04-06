### Working w ith Lists

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("\nThank you, everyone. That was a great magic show!")

## EX 1.
alc = ['Beer', 'Fernet', 'Bailey', 'Singani']
for a in alc:
    print(f"{a} is one alc. beverage I like")
print('But I prefer', alc[0].upper())

ani = ['cats', 'dogs']
for p in ani:
    print(f"{p} have different sizes and colors")
print(" Any of these animals would make a great pet!")

### Making Numerical List
for value in range(1, 5+1):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2)) 
odd_numbers = list(range(1, 11, 2)) 
print(even_numbers, odd_numbers)

squares = [value**2 for value in range(1, 11)]
print(squares)

print(sum(even_numbers), min(even_numbers), max(even_numbers))

## EX 2:
for value in range(1, 20+1):
    print(value)

numbers = list(range(1, int(10e+5)))
print(numbers)
print(sum(numbers), min(numbers), max(numbers))

odd_numbers = list(range(1, 21, )) 
print(odd_numbers)

trees = [x for x in range(3, 31) if x % 3 == 0]
print(trees)

cubes = [x**3 for x in range(3, 11)]
for i in cubes:
    print(i)

## Cube Comprehension: 
print(cubes)

## Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[2:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #siempre se pone al final [:] si no ambas estaran ligadas
print(friend_foods)
print(my_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

## EX 3:

print(f"First elements: {squares[:3]}")
print(f"Middle 3 elements: {squares[3:6]}")
print(f"Last elements: {squares[-3:]}")

my_foods.append('hawaiana')
friend_foods.append('BK')
print(friend_foods)
print(my_foods)

print("Me and my friends have differest tastes on pizza\n My favorite pizzas are:")
for pz in my_foods[-2:]:
    print(pz.title())
print("My friend's favorite pizzas are:")
for pz in friend_foods[-2:]:
    print(pz.title())

print("My favorite pizzas are:")
for pz in my_foods:
    print(pz.title())

### ====== TUPLES ======
# Tuples allow you to do just that. Python refers to values that cannot 
# change as immutable, and an immutable list is called a tuple.

dimensions = (200, 50, 100)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

# EX 4:
sizes = (150, 248, 250, '1T', '2T')
for i in sizes:
    print(i)

sizes[3] = 10000 # rejected

n_sizes = (100, 248, 250, 500, '1T')
print('New list of sizes')
for i in n_sizes:
    print(i)




