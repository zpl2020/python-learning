'''
Unit converter: Miles and Kilometers
'''
def print_menu():
  print('1. Kilometers to Miles')
  print('2. Miles to Kilometers')

def km_miles():
  km = float(input('Enter distance in kilometers: '))
  miles = km / 1.609
  print('Distance in miles: {0}'.format(miles))

def miles_km():
  miles = float(input('Enter distance in miles: '))
  km = miles * 1.609
  print('Distance in kilometers: {0}'.format(km))
if __name__ == '__main__':
  print_menu ()
  choice = input('Which conversion would you like to do?: ')
if choice == '1':
  km_miles ()
if choice == '2':
  miles_km ()

 
  def print_menu():
    print ('1. kmph to mph')
    print ('2. mph to kmph')
  def kmph_mph():
    kmph = float(input('Enter speed in kmph: '))
    mph = kmph / 1.609
    print ('Speed in mph: {0}'.format(mph))

def mph_kmph():
    mph = float(input('Enter distance in mph: '))
    kmph = mph * 1.609
    print ('Speed in kmph: {0}'.format(kmph))
if __name__ == '__main__':
    print_menu ()
    choice = input('Which conversion would you like to do?: ')
if choice == '1':
    kmph_mph ()
if choice == '2':
    mph_kmph ()





'''
Quadratic equation root calculator
'''
def roots(a, b, c):
   D = (b*b - 4*a*c)**0.5
   x_1 = (-b + D)/(2*a)
   x_2 = (-b - D)/(2*a)
   print ('x1: {0}'.format(x_1))
   print ('x2: {0}'.format(x_2))

if __name__ == '__main__':
   a = input('Enter a: ')
   b = input('Enter b: ')
   c = input('Enter c: ')
   a = float(a)
   b = float(b)
   c = float(c)
   roots(float(a), float(b), float(c))
   D = (b*b - 4*a*c)**0.5
   if  D**2 < 0.0:
     print ('inaccessible number')