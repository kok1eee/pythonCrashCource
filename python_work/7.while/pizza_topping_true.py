prompt = "\nいらっしゃいませこんにちは。ピザのトッピングをお伺いします: "
prompt += "\n(終わったら'終了'と入力してください。)"

while True:
    topping = input(prompt)

    if topping == '終了':
        break
    else:
        print(f"{topping}ですね。かしこまりました。")

