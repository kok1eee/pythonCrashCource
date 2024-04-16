filename = 'reason.txt'

while True:
    your_reason = input('なぜあなたはプログラミングが好きなのですか？')

    if your_reason == '終了':
        print("投票終了")
        break
    else:
        with open(filename, 'a',encoding='utf-8_sig') as file_object:
            file_object.write(your_reason)
        print("\n投票ありがとう\n")