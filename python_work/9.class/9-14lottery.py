from random import sample
from random import choice

list = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

class Lottery:
    def lottery(self):
        pick_up_lot = sample(list,4)
        print(f"選ばれた数字は{pick_up_lot}です。")

        return pick_up_lot

    def my_choice(self):
        pick_up_cho = choice(list)
        print(f"あなたが引いたのは{pick_up_cho}です！")

        return pick_up_cho

my_lot = Lottery()

lot = my_lot.lottery()

cho = my_lot.my_choice()

while True:
    if cho in lot:
        print("おめでとう景品が当たりました！")
        break
    else:
        print("残念")

