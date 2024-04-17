import json

def get_stored_number():
    """保存された数字があれば取得する"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def memorized_number():
    """保存されてなければ数字を保存する"""
    favorite_number = input("好きな数字を入れてください。")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def guessed_number():
    """保存されている数字を当てる"""
    favorite_number = get_stored_number()

    if favorite_number:
        print(f"あなたが好きな数字は{favorite_number}ですね！")
    else:
        favorite_number = memorized_number()
        print("好きな数字を教えてくれてありがとう！")

guessed_number()