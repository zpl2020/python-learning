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


class Coordinates():
    def __init__(self, x, y, z):
        self.x = 48
        self.y = 78
        self.z = -123
        self.position = 48, 78, -123

    def actual_position(self):
        print('The actual position of yourself is' + str(self.position) + '.')

#2020/9/7
class Absolute_direction():
    def __init__(self, x, y, z):
        self.x = float(input('Please evaluate:'))
        self.y = float(input('Please evaluate:'))
        self.z = float(input('Please evaluate:'))
        self.position = self.x + self.y + self.z
        self.search_location_time = 0
        self.location_closest_player = (x, y, z)

    def locate(self):
        print('The location of yours is ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '.')

    def search_location_times(self):
        self.search_location_time += 1
        print('The times you have been searching is:' + str(self.search_location_time))

    def location_closest_players(self):
        number_of_players = input('Please enter number of players: ')
        if int(number_of_players) <= 1:
                    self.location_closest_player = str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)
                    print(self.location_closest_player)
        else:
            print('Sorry, but there are multiple players in the zone.')

inst1 = Absolute_direction(x = 12.3, y = 2.5, z = 7.6)
inst2 = Absolute_direction(x = 0.0, y = 0.0, z = 0.0)
inst1.locate()
inst1.location_closest_players()
inst1.search_location_times()
inst2.locate()
inst2.location_closest_players()
inst2.search_location_times()


