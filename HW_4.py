# 5-3: Alien Colors #1
alien_color = 'yellow'

if alien_color == 'yellow':
    print("You just earned 5 points!")

# 5-4: Alien Colors #2

alien_color = 'yellow'

if alien_color == 'yellow':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# 5-5: Alien Colors #3

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")


# 5-6: Stages of Life

age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")


# 5-7: Favorite Fruit

favorite_fruits = ['strawberries', 'peaches', 'blueberries']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")

# 5-8: Hello Admin

usernames = ['Mandy', 'Derek', 'admin', 'Eve', 'Jennies']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")
# 5-9: No Users

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users!")



# 5-10: Checking Usernames


current_users = ['Mandy', 'Derek', 'admin', 'Eve', 'Jennies']
new_users = ['Cinday', 'Olivia', 'Jen', 'Jenny', 'Jackie']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

# 5-11: Ordinal Numbers

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

# 6-1: Person

person = {
    'first_name': 'Emily',
    'last_name': 'Yan',
    'age': 25,
    'city': 'Seattle',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2: Favorite Numbers

favorite_numbers = {
    'Derek': 7,
    'Jenny': 3,
    'Emily': 5,
    'Jackie': 12325,
    'Alicia': 0,
    }


num = favorite_numbers['Derek']
print("Derek's favorite number is " + str(num) + ".")

num = favorite_numbers['Jenny']
print("Jenny's favorite number is " + str(num) + ".")

num = favorite_numbers['Emily']
print("Emily's favorite number is " + str(num) + ".")

num = favorite_numbers['Alicia']
print("Alicia's favorite number is " + str(num) + ".")

num = favorite_numbers['Jackie']
print("Jackie's favorite number is " + str(num) + ".")


# 6-10: Favorite Numbers

favorite_numbers = {
    'Emily': [5, 7],
    'Mandy': [3, 9, 6],
    'Derek': [7, 1],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))
