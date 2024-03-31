# name = input("名前を入力してください: ")
# print(f"\nこんにちは、{name}！")

prompt = "あなたが誰か教えてくれたら、あなた向けのあいさつをします。"
prompt += "\nあなたの名前は？ "


message = ""

while message != '終了':
    message = input(prompt)

    if message != '終了':
        print(message)