## LISTS

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1].title()) ## solo para strings

message = f"My first bicycle was a {bicycles[0].upper()}."
print(message)

friends = ['Joel', 'Carlos', 'Daniel', 'Sergio']
greet = f"Hello dear {friends[1].title()}, how are you?"
print(greet)

core = ['Mini', 'i7', 'None']
wish = f"I would like to have a {core[0]}, but I don't know"
print(wish)

### Changing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

### Adding
motorcycles.append('honda')
print(motorcycles)

### Inserting
motorcycles.insert(4, 'Harley')
print(motorcycles)

## Removing
del motorcycles[0]
print(motorcycles)

# removig the last element
last = motorcycles.pop()
print(f"My last motorcycle was a {last.upper()}")

first = motorcycles.pop(0)
print(f"My first motorcycle was a {first.upper()}")

## Removing by a value
np = core.remove('None')
print(f"This is not a core option: {np}")

core.remove('None')
print(f"This is are the only core options: {core}")

## EX 1.
guests = ['A', 'V', 'D', 'G', 'F']
nc = guests.pop(-2)

print(f"Invited guest: {guests}")
print(f"Not comming: {nc}")

for i in guests:
    print(f"{i} are inveted to my party")

guests.append('W')
guests.insert(0,'Q')
guests.insert(0,'E')

for i in guests:
    print(f" Dear {i}, you are inveted to my party\n my house is big!!!")

s1 = guests.pop(1)
s2 = guests.pop(-3)

print(f"{s1, s2} you are special guests to my party")

### SORTING
cars = ['bmw', 'audi', 'toyota', 'subaru', 'mercedez']
cars.sort(reverse=True)
print(cars)
print(sorted(cars,reverse=True))

cars.reverse()
print(cars)

## EX 2
vis = ['Bol', 'Spn', 'Fra', 'Ger']
print(vis)

print(sorted(vis))
print(vis)

vis.reverse()
print(vis)

vis.sort()
print(vis)

vis.sort(reverse=True)
print(vis)

print('Number of guests:', len(guests))

## AVOID INDEXING ERRORS
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[-3])


