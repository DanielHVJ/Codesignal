## Dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# add variables
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

## program
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
 # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# delete
del alien_0['speed']
print(alien_0)

alien_0['color'] = 'red'
alien_0['speed'] = 'fast'
print(alien_0)
point_value = alien_0.get('points', 'No point value assigned.') # get() default vallue even not assigned
print(point_value)

## EX1
person = {'name': 'Jill', 'age': 23, 'city': 'Reacon City'}
for i in person:
    print(i.title(),':',person[i])

numbers = {'Jill': 23, 'John': 43, 'Will': 12}
for i in numbers:
    print('Favorite numbers\n',i,':',numbers[i])

pr = {'Data structures': 'main functions: add, rm, append, etc', 'Pandas': 'Review', 'Numpy': 'almost from scratch', 'algotihms':'more notions'}

print('Python keep learning')
for i in pr:
    print(i,':\n\t',pr[i])


# Key and Value: the correct way
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.upper()}.")

-- 139