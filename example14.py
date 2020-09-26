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

def complex_calculation(a, b, c, d):
    return a**(1/3) + b * (c - d)

class Coin():
    def __init__(self):
        self.face = 2

    def flip_coin(self, x):
        self.face = x

if __name__ == '__main__':
    x = randint(1, 6)
    inst1 = Dice()

    for value in range(0, 100):
        x = randint(1, 6)
        inst1.roll_die(x)

    inst1.print_sides()
    x = randint(1,2)