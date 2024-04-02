prompt = "\nいらっしゃいませこんにちは。ピザのトッピングをお伺いします: "
prompt += "\n(終わったら'終了'と入力してください。)"

active = True
while active:
    message = input(prompt)

    if message == '終了':
        active = False
    else:
        print(message)