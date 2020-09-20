class Die():
    
    def __init__(self, sides,  predictions):
        self.sides = sides
        self.predictions = predictions

    def roll_dice(self):
        from random import randint
        percentage = randint(1, self.sides)
        print(str(percentage))


A = str(input('Enter the number of sides.'))
C = str(input('Enter your predictions.'))
inst1 = Die(A, C)
inst1.roll_dice()
inst1.roll_dice()
inst1.roll_dice()