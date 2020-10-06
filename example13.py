from collections import OrderedDict

myOrderedDict = OrderedDict()
myOrderedDict['A'] = 'Python'
myOrderedDict['B'] = 'C++'
myOrderedDict['C'] = 'Somers'
myOrderedDict['D'] = 'c'

for name, language in myOrderedDict.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')

from random import randint
class Coin_flip():
    from random import randint
    def __init__(self, sides, flip_attempts):
        self.sides = sides
        self.flip_attempts = 0
    def flip_results(self):
        self.sides = randint(1,2)
        print ('The side is ' + self.sides + '.')
    def increment_flip_attempts(self):
        self.flip_attempts += 1
        print('The times you have been trying is: ' + self.flip_attempts + '.')


A = input('Enter number of sides: ')
B = input('Enter flip attempts: ')
inst1 = Coin_flip(A, B)
inst1.increment_flip_attempts()
inst1.increment_flip_attempts()
inst1.increment_flip_attempts()
inst1.increment_flip_attempts()
inst1.increment_flip_attempts()