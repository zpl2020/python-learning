number = int(input('Enter a number'))
if number % 10 == 0:
  print('True.')
else:
  print('False.')


response = int(input('How many people will join the party?'))
people = int(number)
if response <= 6:
  print('We still have vacancies.')
else:
  print('Sorry, but we do not have enough seats.')

pizza_toppings = input('What do you want for a pizza topping?')
if pizza_toppings == ['Tomato', 'Sardines', 'Cheese', 'Bacon']:
  print('We are preparing for a ' + pizza_toppings + '-topped pizza.')
else:
  print('Sorry, but we do not have this pizza topping.')


age = int(input('How old are you?'))
if age <= 7:
  print('Free of charge.')
if 8 <= age <= 18:
  print('Please pay 4 dollars.')
if 60 <= age <=100:
  print('Free of charge.')
else:
  print('Please pay 14 dollars.')


number = int(input('Enter your number.'))
if number % 2 ==0:
  print('Is an even number.')
else:
  print('Is an odd number.')


username = str(input('Enter your name.'))
def greet_user ():
  global username
  print('Hello, user ' + username + '.')

greet_user()


messages = '123'
def display_messages():
  print('The passage exerpt is relevant to ' + messages + '.')

display_messages()


def describe_city(city, nation):
  print(city + ' is located in ' + nation + '.')

describe_city