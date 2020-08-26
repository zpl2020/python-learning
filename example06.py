names = ['A', 'B', 'C', 'D']
print (names [0])
motorcycles = ['Honda', 'Yamaha', 'Kawasaki']
last_owned = motorcycles.pop(0)
print ('The first motorcycle I owned as a ' + last_owned.title() + '.')
Message = 'Hello Python World!'
print (Message)
magicians = ['Fudge', 'David', 'Boop']
for magician in magicians:
  print(magician.title()+", that was a great trick!")
  print("I can't wait to see your next trick, "+ magician.title() + ".\n")

result = []
for value in range (0, 15):
  result = value**3
  print (result)

languages = ['English', '中文', 'Espaniol', 'Deusch']
print ("The languages supported are: "+ languages[0], languages[1], languages[3] + ".")
print ("The last supported languages are: " + languages[-1], languages[-2], languages[-3] + ".")
languages.append ('Italia')
for language in languages[:4]:
  print (language.title())

A = (1, 2, 3, 4, 5, 6, 7, 8)
print (A[0])

industries = ['Vought', 'Boeing', 'Kawasaki', 'Mitsubishi', 'Messechmmit']
for industry in industries:
  if industry == 'Vought':
    print(industry.upper())
  else:
    print(industry.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
  print('Hold the anchovies.')

age = 12

if age < 4:
  price = 0
  print('It\'s for free.')
elif age < 18:
  price = 5
  print('Five dollars, please.')
elif age < 65:
  price = 10
  print('Ten dollars, please.')
elif age > 65:
  price = 5
  print('Five dollars, please.')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print('Sorry, we ran out of green peppers now.')
  else:
    print('Adding' + ' ' + requested_topping + '.')
print('\nFinished making your pizza!')

inputs = ['admin', 'Eric', 'Vacant']
for input in inputs:  
  if input == 'admin':
    print('Hello ' + inputs[0] + '.')
  if input == 'Eric':
    print('Hello ' + inputs[1] + '.')
  else:
    print(inputs[2] + ', ' + 'we must find more users' + '.')

l = []

for i in range (1, 10):
  l.append(i)
print (l)
for l in range (1, 10):
  print (l)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
  if number == 1:
    print('1st.')
  elif number == 2:
    print('2nd.')
  elif number == 3:
    print('3rd.')
  else:
    print(str(number) + 'th.')

alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

character_0 = {'x_position':0, 'y_position':70, 'speed':'fast'}
print('Original x-position: ' + str(character_0['x_position']))
if character_0['speed'] == 'slow':
  x_increment = 1
elif character_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3
character_0['x_position'] = character_0['x_position'] + x_increment
print("New x-position: " + str(character_0['x_position']))

details = {'first_name':'Erich', 'last_name':'Haster', 'age':44, 'city':'Smolensk'}
print('identity: ' + str(details['first_name']) + ' ' + str(details['last_name']))

favourite_languages = {
 'jen': 'python',
 'sarah': 'c',
  'phill': 'ruby',
  }
friends = ['phill', 'jen']
for name in favourite_languages.keys():
  print(name.title())

  if name in friends:
    print('Hi ' + name.title() + ', I see your favourite language is ' + favourite_languages[name].title() + '!')

rivers = {'Nile':'Egypt', 'Amazon':'Brazil', 'Yangze River':'China'}
for key, value in sorted(rivers.items()):
  print('The ' + key + ' flows through ' + value)


names = {'name':'J', 'language':'E'}
names['name'] = 'J, H'
names['language'] = 'E, G'
a = names['name']
b = names['language']
print(names)
print(str(a) + '\'s favourite language are ' + str(b) + '.')
print(str(a) + ', thank you for participating in our survey.')

applicants = {
  'MH':{
    'first': 'Mycroft',
    'last': 'Holmes',
    'location': 'Office',
  },
  'JM':{
    'first': 'James',
    'last': 'Moriarty',
    'location': 'Barts',
  },
}
for applicants, applicant_info in applicants.items():
  print('\napplicants: ' + applicants)
  full_name = applicant_info['first'] + ' ' + applicant_info['last']
  location = applicant_info['location']
  print('\tFull name: ' + full_name.title())
  print('\tLocation: ' + location.title())
	
