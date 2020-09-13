def roots(a, b, c):
   D = (b*b - 4*a*c)**0.5
   x_1 = (-b + D)/(2*a)
   x_2 = (-b - D)/(2*a)
   print('x1: {0}'.format(x_1))
   print('x2: {0}'.format(x_2))



if __name__ == '__main__':
   a = input('Enter a: ')
   b = input('Enter b: ')
   c = input('Enter c: ')
   roots(float(a), float(b), float(c))

from fractions import Fraction
try:
  f = Fraction(input('Enter f: '))
except (ZeroDivisionError,ValueError):
  print('Please enter an appropriate number.')
print (f)



def factors(b):
  for i in range(1, b+1):
    if b % i == 0:
      print(i)
if __name__ == '__main__':
  b = input('Your Number Please: ')
  b = float(b)
  if b > 0 and b.is_integer():
     factors(int(b))
  else:
     print('Please enter a positive integer')



'''
Multiplication table printer
'''
def multi_table(a):
  for i in range(1, 11):
      print('{0} x {1} = {2}'.format(a, i, a*i))
if __name__ == '__main__':
   a = input('Enter a number: ')
   multi_table(float(a))

your_user = User('G', 'H', 'Male')
long_name = "abc"
print("Hello", your_user.get_descriptive_name())
print ("This is test:", long_name)
your_user.greet_user()

my_user = User('L', 'L', 'Male')

my_user.login_attempts()
my_user.login_attempts()
my_user.login_attempts()
my_user.login_attempts()
my_user.display()

import matplotlib.pyplot as mplt
import numpy as np
t = np.arange(0., 5., 0.2)
mplt.plot(t, t, 'r--', t, t**0.5, 'bs', t, t**(1/3), 'g^')
mplt.show()

class Light():
    def __init__(self, size, flexibility, battery_size):
        self.size = size
        self.flexibility = flexibility
        self.battery_size = 800

    def get_descriptive(self):
        self.size

