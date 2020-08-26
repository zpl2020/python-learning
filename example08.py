while True:
  age = int(input('How old are you?'))
  if age <= 7:
    print('Free of charge.')
    break
  elif 8 <= age <= 18:
    print('Please pay 4 dollars.')
  elif 60 <= age <=100:
    print('Free of charge.')
  else:
    continue
 

i = int(input('Enter random number.'))
while True:
  if i > 0:
    print('This is a positive integer')
    break
  elif i < 0:
    print('This is a negative integer.')
  elif i == 0:
    print('This is an integer.')
  else:
    print('Please enter a supported number.')
    continue


def describe_city(city, state, nation):
  print(city + ' is located in ' + state + ', ' + nation + '.')

describe_city(city = 'Des Moines', state = 'Iowa', nation = 'United States')


def make_shirt(shirt_size, shirt_words):
  print('The shirt is sized ' + shirt_size + '.')
  print('The words on this shirt says: ' + shirt_words + '.')

make_shirt(shirt_size = '04', shirt_words = 'Life is like a box of chocolates')


def get_formatted_name(first_name, middle_name, last_name):
  full_name = first_name + ' ' + middle_name + ' ' + last_name
  return full_name.title()

celebrity = get_formatted_name('Johnathan', 'Cutler', 'Beckett')
print(celebrity)


original_magicians = ['John', 'Moffat', 'Mark']
new_magicians = []
for magician in original_magicians:
  magician = 'The great ' + magician
  new_magicians.append(magician)
print(new_magicians)

def show_magicians():
  print('The great ' + str(new_magicians[0:3]) + '.')

show_magicians()


def pizza_toppings():
  print('A', 'B', 'C', 'D', 'E')
import pizza_toppings as pt
pt