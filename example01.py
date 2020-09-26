def is_factor(a, b):
  if b % a == 0:
    return True
  else:
    return False

print(is_factor(11, 3))
def is_factor2(x, y):
 if y == x**2 - x*2:
   return True
 else:
  return False
print (is_factor2(3,0))



from fractions import Fraction
a = Fraction(input('enter a number:'))
print (a)



z = complex(input('Enter a complex number: '))
print (z)



for i in range (-10, 10):
    print (i)

def factors(b):
   for i in range(1, b+1):
    if b % i == 0:
     print(i)

if __name__ == '__main__':
  b = input('Your Number Please: ')
  b = float(b)
  if b > 0 and b.is_integer():
    factors (int(b))
  else:
    print('Please enter a positive integer')


F = 98.6
print (F - 32) * (5 / 9)