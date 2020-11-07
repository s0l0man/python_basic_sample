# name = input("Enter name of Patient: ")
# age = input("")
# is_new = True
# print("Patient :" + str(name) + "\nAge :" + str(age) + "\nIs he new :" + str(is_new))

# name = input('What is your name? ')
# fav_color = input('What is your Favorite color? ')
# print(name + " like " + fav_color)

# birth_year = int(input('Birth year: '))
# age = 2020 - birth_year
# print('Your age is : ' + str(age))

# weight = int(input('Enter your weight: '))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == 'K':
#     converted = weight * 0.45
#     print('Weight in Kg is: ' + str(converted))
# else:
#     converted = weight / 0.45
#     print('Weight in lbs is: ' + str(converted))

# course = 'Python for Beginner'
# print(course[1:-1])

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder' #to define formatted string prefix with f and use {} to dynamically insert values into your string
# print(msg)

# course = 'Python for Beginners'
# print(len(course)) #len is a function
# print(course.upper()) #method
# print(course.lower()) #method
# print(course.find('g')) #method
# print(course.replace('Beginners','Absolute Beginners')) #method
# print('python' in course) #operator

# x = 10 + 3 * 2 ** 2 # operator precedence
# print(x)
# import math
# print(math.fabs(10)) # math module for performing mathematical calculation
# x = -2.9
# print(abs(x)) #  math module in Python for calculating mathaematical problem

# price = 10000000
# has_good_credit = False
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Download payment :${down_payment}")

# has_good_credit = True
# has_criminal_record = True
# if has_good_credit and not has_criminal_record: # logical operator
#     print("Eligible for loan")
# else:
#     print("Not eligible for load :(")

# name = input("Enter your name: ")
#
# if len(name.upper()) <3:
#     print('Name must be 3 characters')
# elif len(name) >50:
#     print("Name can be maximum of 50 characters")
# else:
#     print("name looks good")

# secret_number = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!!")
#         break
# else:
#     print("Sorry you failed!!!")

# command = ""
# started = False
# while True:
#     command = input("> ".lower())
#     if command =="start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command =="stop":
#         if not started:
#             print("Car already stopped!")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that!")

# prices = [10,20,30]
# total = 0
# for price in prices: #For loop
#     total += price
# print(f"Total: ${total}")

# for x in range(4):
#     for y in range (3):
#         print(f'({x},{y})')


# numbers1 = [2,2,2,2,8]
# for x_count in numbers1:
#     print(x_count * 'x')
# print()
# print()
# numbers1 = [5,2,5,2,2]
# for x_count in numbers1:
#     print(x_count * 'x')

# names = ['John','Bob','Sarah','Marry']
# names2 = names.copy()
# names[0] = 'Jon'
# names.append('Alex')
# names.insert(1,'Tom')
# names2.sort()
# names2.reverse()
# print(f'first name list is : {names} \nsecond name list is : {names2}')

# numbers = [8,4,7,10,12,100,10,20]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max = num
# print(max)

# matrix1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix1:
#     for items in row:
#         print(items)

# names = ['John','Bob','Sarah','Marry','John','Bob']  #find duplicate
# find = []
# for dup in names:
#     if dup not in find:
#         find.append(dup)
# print(find)

# #Tuples are immutable example of unpacking
# coordinates = (1,2,3)
# x,y,z = coordinates
# print(z)

# customer = {
#     "name": "john smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer.get("name"))
# print(customer.get("birthdate","Jan 20 1980"))

def number_text_conversion(num):
    digit_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three"
    }
    output = ""
    for ch in {num}:
        output += digit_mapping.get(ch, "!") + " "
    print(output)


# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "😒",
#     ":|": "😐",
#     ":/": "😕",
#     ":?": "🤔",
#     ":*": "😘"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

def emoji_convertor(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒",
        ":|": "😐",
        ":/": "😕",
        ":?": "🤔",
        ":*": "😘",
        "Hey": "Hi! How are you?",
        "good": "Glad to hear from you",
        "help": "How can i help you today!"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output.title()


def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcome aboard!")


def square(number):
    return number * number


def error_handling():
    try:
        age = int(input('Age: '))
        income = 20000
        risk = income / age
        print(age)
        print(risk)
    except ZeroDivisionError:
        print('Age cannot be 0')
    except ValueError:
        print('Invalid value')


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print('#')

    def draw(self):
        print('*')


point = Point(10,20)
print(point.x)


class Mammal:
    def walk(self):
        print("walk")


class dog(Mammal):
    def bark(self):
        print("bark")
    pass


class cat(Mammal):
    def be_annoying(self):
        print("annoying")
    pass

import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())

import pandas as pd

music_data = pd.read_csv('music.csv')
x = music_data.drop(columns=['genre'])
y = music_data['genre']

