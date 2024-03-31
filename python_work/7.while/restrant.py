guest = input("ディナーには何人参加しますか？ ")
guest = int(guest)

if guest >= 8:
    print(f"{guest}名様ですね、席に着くまで少しお待ちください。")
else:
    print(f"{guest}名様ですね、テーブルの準備ができております。")