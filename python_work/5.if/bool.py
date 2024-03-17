car = 'subaru'

# carにはsubaruが入っているためcar == subaruはTrue
print("car == 'subaru'の結果を True と予測します。")
print(car == 'subaru')

# carにはsubaruが入っているためcar == audiはFalse
print("\ncar == 'audi'の結果を False と予測します。")
print(car == 'audi')


style = 'lager'

print("style == 'lager'の結果をTrueと予測します。")
print(style == 'lager')

print("style == 'ale'の結果をFalseと予測します。")
print(style == 'ale')

animal = 'cat'

print("animal == 'cat'の結果をTrueと予測します")
print(animal == 'cat')

print("animal == 'cat'の結果をfalseと予測します")
print(animal == 'dog')


# 文字列の一致と不一致のテスト

name = 'masayoshi'

print("name = 'masayoshi'の結果をTrueと予測します。")
print(name == 'masayoshi')

print("name = 'tazawa'の結果はFalseと予測する。")
print(name == 'tazawa')

print("name.lower() == 'masayoshi'の結果をTrueと予測する。")
print(name.lower() == 'masayoshi')

print("name.upper() == 'masayoshi'の結果をFalseと予測する")
print(name.upper() == 'masayoshi')

print("name.upper() == 'MASAYOSHI'の結果をTrueと予測する。")
print(name.upper() == 'MASAYOSHI')

number = 911
print("等しい")
print(number == 911)

print("小さい")
print(number < 900)
print(number < 912)

print("大きい")
print(number > 900)
print(number > 912)

print("以下")
print(number <= 912)
print(number <= 910)

print("以上")
print(number >= 912)
print(number >= 910)

print("and")
print(number < 912 and number > 910)
print(number < 910 and number > 912)

print("or")
print(number < 910 or number == 911)


print("for")
yugiohs = ['original','gx','5ds']

print('duel_monsters' in yugiohs)
print('gx' in yugiohs)

my_favorite_card_game = 'duel_monsters'
print(my_favorite_card_game not in yugiohs)
print('gx' not in yugiohs)