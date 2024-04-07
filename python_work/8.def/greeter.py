def greet_user(username):
    """シンプルな挨拶メッセージを出力する"""
    print(f"こんにちは{username.title()}！")

greet_user("masayoshi")

def get_formatted_name(first_name,last_name):
    """フォーマットされたフルネームを返す"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# これは無限ループです！

while True:
    print("\nあなたの名前を教えてください。")
    print("qを入力すると終了します。")

    l_name = input("姓を教えてください。")
    if l_name == "q":
        break

    f_name = input("名を教えてください。")
    if f_name == "q":
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nこんにちは{formatted_name}")