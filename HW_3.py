# 3-1: Names

print("3-1 Names")
names = ['Lexi', 'Jen', 'Andy']

print(names[0])
print(names[1])
print(names[2])

print("\n3-2 Greetings")

for name in names:
  msg = "Hello, " + name.title() + "!"
  print(msg)

print("\n3-4 Guest List")

guests = names

for guest in guests:
  msg = "Hello, " + guest.title() + " ,please come to the party!"
  print(msg)


print("\n3-5 Changing Guest List")

# Invite some people to dinner.
guests = names

for guest in guests:
  msg = "Hello, " + guest.title() + " ,please come to the party!"
  print(msg)

print("\nSorry, " + guests[1].title() + " can't make it to dinner.")

# Jen can't make it! Let's invite Tom instead.
del(guests[1])
guests.insert(1, 'Tom')

# Print the invitations again.
for guest in guests:
  msg = "Hello, " + guest.title() + ", please come to the party"
  print(msg)

print('\n')
print("3-6 More Guests")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Added friend 1')
guests.insert(2, 'Added friend 2')
guests.append('Added friend 3')

for guest in guests:
  msg = "Hello, " + guest.title() + ", please come to the party!"
  print(msg)
print('\n')


print('3-7 Shrinking Guest List')

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

while (len(guests) > 2):

    name = guests.pop()
    print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
for guest in guests:
  msg = "Hello, " + guest.title() + ", please come to the party!"
  print(msg)

# Empty out the list.

while (len(guests) > 0):
    del(guests[0])

# Prove the list is empty.
print(guests)
print('\n')

print('3-8 Seeing the World')

locations = ['Spain', 'Iceland', 'Greece', 'Japan', 'Korea']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)
print('\n')

print('4-1 Pizzas')

favorite_pizzas = ['Hawaiian', 'Cheese', 'Mushroom']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print("My favorite pizza is " + pizza + " pizza!")
print('\n')
print('4-3: Counting to Twenty')
numbers = list(range(1, 21))

for number in numbers:
    print(number)
print('\n')
print('4-5: Summing a Million')
numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('\n')

print('4-8: Cubes')
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print('\n')

print('4-9: Cube Comprehension')
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)
print('\n')


print('4-11: My Pizzas, Your Pizzas')
favorite_pizzas = ['Hawaiian', 'Cheese', 'Mushroom']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("Sausage")
friend_pizzas.append('Tomato')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
print('\n')
print('part B')
favorite_foods = ['burgers','pizzas','cakes']
print('original list: ')
print(favorite_foods)

new_food = raw_input('enter your favorite food!')
favorite_foods.append(new_food)
print('\n')
print('new list: \n')
print(favorite_foods)
