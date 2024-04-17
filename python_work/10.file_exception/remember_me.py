import json

def get_stored_username():
    """以前に保存されたユーザー名があれば読み込む"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("あなたのお名前は？")
    filename = 'username.json'
    
    with open(filename,'w') as f:
            json.dump(username, f)
    return username

def greet_user():
    """ユーザー名であいさつする"""
    username = get_stored_username()
    if username:
        print(f"おかえりなさい、{username}さん！")
    else:
        username = get_new_username()
        print(f"戻ってきたときにも名前を憶えていますよ、{username}さん！")
    
greet_user()