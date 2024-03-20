user_lists = []

if user_lists:
    for user_list in user_lists:
        if user_list == 'admin':
            print(f"こんにちは{user_list}、状況のレポートを見ますか？")
        else:
            print(f"こんにちは{user_list}、またログインしてくれてありがとう。")
else:
    print("ユーザー募集中です！")

current_users = ['a','b','c','d','e']

new_users = ['a','b','f','g','h','A','B']

for new_user in new_users:
    new_user = new_user.lower()
    
    if new_user in current_users:
        print(f"すでに{new_user}は使われています。")
    else:
        print(f"こちらの{new_user}は利用可能です。")
