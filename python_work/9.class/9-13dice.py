from random import randint

class Die:
    """サイコロの情報を表すクラス"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """サイコロを振る"""
        return randint(1,self.sides)

    def change_sides(self,sides):
        self.sides = sides

my_die = Die()

# my_die.change_sides(10)

my_die.change_sides(20)

for i in range(10):
    print(my_die.roll_die())# print(my_die.roll_die())