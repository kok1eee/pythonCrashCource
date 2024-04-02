prompt = "\nいらっしゃいませこんにちは。ピザのトッピングをお伺いします: "
prompt += "\n(終わったら'終了'と入力してください。)"

topping = ""
while topping != '終了':
    topping = input(prompt)

    if topping != '終了':
        print(topping)