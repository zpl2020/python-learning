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



