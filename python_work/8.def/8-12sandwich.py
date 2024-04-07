def make_sandwich(*toppings):
    """注文されたトッピングのサンドイッチを出力する"""
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('トマト')

sandwich_list = ['ツナ','トマト','チーズ']

make_sandwich(sandwich_list)

make_sandwich('ツナ','トマト','チーズ')