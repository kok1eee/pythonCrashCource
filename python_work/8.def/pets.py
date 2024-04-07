# def describe_pet(animal_type,pet_name):
#     """ペットについての情報を出力する"""
#     print(f"\n私は{animal_type}を飼っています。")
#     print(f"{animal_type}の名前は{pet_name}です。")

# describe_pet("ネコ","ミミ")
# describe_pet("ハムスター","ハム太郎")

# # キーワード引数を使って表示

# describe_pet(animal_type='フェレット',pet_name='セブン')

def describe_pet(pet_name,animal_type='イヌ'):
    """ペットについての情報を出力する"""
    print(f"\n私は{animal_type}を飼っています。")
    print(f"{animal_type}の名前は{pet_name}です。")

describe_pet(pet_name='ウィリー')