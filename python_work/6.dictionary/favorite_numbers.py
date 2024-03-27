favorite_numbers = {
    'itadori':1,
    'megumi':22,
    'nobara':4,
    'toge':9,
    'maki':6,
    'satoru':22
    }

for favorite_number in favorite_numbers:
    number = favorite_numbers[favorite_number]

    print(f"{favorite_number}の好きな番号は{number}です。")

favorite_numbers = {
    'itadori':[1,2],
    'megumi':[4,22,100],
    'nobara':[3,10],
    'toge':9,
    'maki':[6,15,24],
    'satoru':[30,50],
    }

for person,numbers in favorite_numbers.items():
    print(f"{person}の好きな数字は{numbers}です。")