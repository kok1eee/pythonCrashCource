number = input("好きな数字を入れてください。それが10の倍数か判定します。")

number = int(number)

if number % 10 == 0:
    print(f"{number}は10の倍数です。")
else:
    print(f"{number}は10の倍数ではありません。")