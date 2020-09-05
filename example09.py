class Restaurant():
    def __init__(self, client, popularity):
        self.client = client
        self.popularity = popularity

    def get_descriptive_name(self):
        long_name = str(self.client) + ' ' + self.popularity
        return long_name.title()

Restaurant = Restaurant('A', '2564/4000')
print(Restaurant.get_descriptive_name())

class User():

    def __init__ (self, first_name, last_name, gender, number_of_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.number_of_attempts = 0

    def get_descriptive_name(self):
        self.long_name = str(self.first_name) + ' ' + self.last_name + ' ' + self.gender
        return self.long_name.title()

    def greet_user(self):
        # global long_name
        print('Hello ' + self.long_name + '.')
        
    def login_attempts(self):
        self.number_of_attempts += 1

    def display(self):
        print(self.number_of_attempts)

    def reset_login_attempts(self):
        self.number_of_attempts = 0

    def feed_food(self, food_type):
        self.take_food = food_type

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

class Coordinates():
    def __init__(self, x, y, z):
        self.x = 48
        self.y = 78
        self.z = -123
        self.position = 48, 78, -123

    def actual_position():
        print('The actual position of yourself is' + str(self.position) + '.')