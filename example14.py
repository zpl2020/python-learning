from random import randint

class Dice():
    def __init__(self):
        self.side = 6
        self.count_on_side1 = 0
        self.count_on_side2 = 0
        self.count_on_side3 = 0
        self.count_on_side4 = 0
        self.count_on_side5 = 0
        self.count_on_side6 = 0

    def roll_die(self, x):
        self.side = x
        print(self.side)
        if x == 1:
            self.count_on_side1 += 1
        elif x == 2:
            self.count_on_side2 += 1
        elif x == 3:
            self.count_on_side3 += 1
        elif x == 4:
            self.count_on_side4 += 1
        elif x == 5:
            self.count_on_side5 += 1
        elif x == 6:
            self.count_on_side6 += 1
    
    def print_sides(self):
        print ('Side 1: ' + str(self.count_on_side1))
        print ('Side 2: ' + str(self.count_on_side2))
        print ('Side 3: ' + str(self.count_on_side3))
        print ('Side 4: ' + str(self.count_on_side4))
        print ('Side 5: ' + str(self.count_on_side5))
        print ('Side 6: ' + str(self.count_on_side6))



class Coin():
    def __init__(self, count_on_face, face):
        self.face = 2
        self.count_on_face1 = 0
        self.count_on_face2 = 0
   
    def flip_coin(self, x):
        self.face = x
        print(self.face)
        if x == 1:
            self.count_on_face1 += 1
        elif x ==2:
            self.count_on_face2 += 1
    
    def print_faces(self):
        print ('Face 1: ' + str(self.count_on_face1))
        print ('Face 2: ' + str(self.count_on_face2))