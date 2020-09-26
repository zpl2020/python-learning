x=10
y = oct(x )
print(y)

if __name__ == '__main__':
        print(eval ('3+2+1'))

import math
y=dir (math)
print (y)

x=3**0.5
y=math.atan(x)
print (math.degrees(y))

print ('This is a funny\n story I\'d like to hear\a\a\a\a\a\a')

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print (tup3)


import operator
A = [ 1,2,3,4,5]
B = [ 5,6,7 ]
operator.eq(A, B)
print (A in B)



a = 10
b = a
print (a)
print (b)
b = 20
print (a)
print (b)

for i in range (2,14):
  print (i)
  a = 2**64
  b = 1
  if (a-b)%i == 0:
    print  ('is a composite number')
  else:
    print  ('is a prime number')

import time
 
localtime = time.localtime(200000000000)
print("本地时间为 :", localtime)




import calendar
cal = calendar.month(2019, 2)
print ("以下输出2019年2月份的日历:")
print (cal)


def printme(str):
   "打印任何传入的字符串"
   print (str)
   return
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")



def ChangeInt():
  global b
  b = 10
 
b = 2
ChangeInt()
print (b)



def bacon():
  global eggs
  eggs = 'bacon' # this is the global
eggs = 45 # this is the global
bacon()
print(eggs)



def spam(divide_by):
  try:
    return 42 /divide_by
  except ZeroDivisionError:
    print('Error: Invalid argument')
    return 'N/A'

print (spam(2))
print (spam(12))
print (spam(0))
print (spam(1))



import random
secret_number = random.randint(1, 20)
print ('I am thinking of a number between 1 and 20.')
# Ask the player to guess six times.
for guesses_taken in range(1,7):
  print('Take a guess.')
  guess = int(input())
  
  if guess < secret_number:
    print('Higher.')
  elif guess > secret_number:
    print('Lower.')
  else:
      break # This condition is the correct guess!
if guess == secret_number:
  print('Good job.')
else:
  print('Nope, the answer was ' + str(secret_number))



def changeme( mylist1 ):
   "修改传入的列表"
   mylist1.append(1)
   print ("函数内取值: ", mylist1)
   return
 

mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)



def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出:")
   print (arg1)
   for var in vartuple:
      print (var)
   return
printinfo(10)
printinfo(70, 60, 50)




Sum = lambda arg1,arg2 : arg1 + arg2
print ("The result of addition is:", Sum ( 10, 20 ))
print ("The result of addition is:", Sum ( 20, 20 ))



name = 'Zophie'
print (name[0:4])



import sys
print (sys.path)



Money = 2000
def AddMoney():
   # global Money
   Money = 1000
   Money = Money + 1
 
print (Money)
AddMoney()
print (Money)