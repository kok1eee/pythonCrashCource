def greet_users(names):
    """リストの各ユーザーに対してシンプルな挨拶を出力する"""
    for name in names:
        msg = f"こんにちは{name.title()}!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)