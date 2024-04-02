prompt = "いらっしゃいませ、お客様の年齢をお伺いします。"
prompt += "人数の入力が終わりましたら'終了'をお願いします。"

while True:
    old = input(prompt)
    old = int(old)

    if old == '終了':
        break
    elif old <= 3:
        print(f"{old}歳は無料になります。")
    elif old <= 12:
        print(f"{old}歳は子供料金で1000円になります。")
    elif old < 60:
        print(f"{old}歳は大人料金で1500円になります。")
    elif old >=60:
        print(f"{old}歳はシニア料金で1000円になります")
    else:
        print(f"ちゃんと入力してください。")