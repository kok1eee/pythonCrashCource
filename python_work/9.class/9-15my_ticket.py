from random import sample

class Lottery:
    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
        self.count = 0

    def pick_up(self):
        pick_up_lot = sample(self.list,4)
        return pick_up_lot

    def winning_number(self):
        wn = sample(self.list,4)
        return wn

lot = Lottery()

win_ticket = lot.winning_number()

print(f"当選番号は{win_ticket}です！")

while True:
    my_ticket = lot.pick_up()
    print(f"あなたのチケット:{my_ticket}")
    lot.count += 1

    if my_ticket != win_ticket:
        print("残念、もう一度くじを引いてください。")
    else:
        print("景品が当たりました")
        print(f"当選までに{lot.count}回くじを引きました。")
        break


