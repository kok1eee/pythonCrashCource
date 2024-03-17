father = 31
mother = 33
girl = 3
boy = 1

age = 64

if age <= 4:
    print("4歳未満は入場料は無料です。")
elif age < 18:
    print("18歳未満の入場料は2500円です。")
else:
    print("18歳以上の入場料は4000円です。")

if age <= 4:
    price = 0
elif age < 18:
    price = 2500
elif age < 65:
    price = 4000
elif age >= 65:
    price = 2000

print(f"入場料金は{price}円です。")