# import module_name
# import ファイル名
# import pets_function
# pets_function.describe_pet(animal_type='フェレット',pet_name='セブン')


# from module_name import function_name
# from ファイル名 import 関数名
# from pets_function import describe_pet
# ファイル名から関数をインポート
# describe_pet(animal_type='フェレット',pet_name='セブン')

# from module_name import function_name as fn
# from ファイル名 import 関数名 as 短縮した関数名
# from pets_function import describe_pet as pf
# 短縮した関数名だけで関数を呼び出せる
# pf(animal_type='フェレット',pet_name='セブン')

# import module_name as mn
# import ファイル名 as 短縮したファイル名
# import pets_function as pf
# ファイル名を短縮したファイル名としてインポート
# pf.describe_pet(animal_type='フェレット',pet_name='セブン')

# from module_name import *
# from ファイル名 import *(モジュールの全関数)
from pets_function import *
# ファイル名から全関数をインポートする
describe_pet(animal_type='フェレット',pet_name='セブン')