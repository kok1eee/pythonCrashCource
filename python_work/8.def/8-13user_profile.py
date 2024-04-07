def build_profile(first,last,**user_info):
    """ユーザーの全情報を格納した辞書を作成する"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('masayoshi','tazawa',
                            location='足立区',
                            field='営業',
                            hobby='クラフトビール',
                            children=2
                            )
print(user_profile)
