import example14
import random

inst1 = example14.Dice()
inst1.roll_die(random.randint(1,6))


from example14 import Dice
from random import randint
if __name__ == '__main__':
    x = randint(1, 6)
    inst1 = Dice()

    for value in range(0, 100):
        x = randint(1, 6)
        inst1.roll_die(x)

    inst1.print_sides()
    x = randint(1,2)


def complex_calculation(a, b, c, d):
    return a**(1/3) + b * (c - d)