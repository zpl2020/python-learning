Money = 2000
def AddMoney(result):
   # global Money
   Money = 1000
   result = Money + 1
   print (result)
   return result

print (Money)
print (Money)



def ChangeInt( a ):
    a = a - 1
    if a > 0:
      print (a)
      ChangeInt(a)
    else:
      return

a = 10
b = 2
ChangeInt ( a )
ChangeInt ( b )



import time
ticks = time.time()
print ( 'Current Time is:', ticks )



import time
 
localtime = time.asctime( time.localtime(time.time()) )
print ("Current time is:", localtime)



for x in range (0, 5):
  print (x)