from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self, rolls):
        for x in range(rolls):
            print(randint(1, self.sides))