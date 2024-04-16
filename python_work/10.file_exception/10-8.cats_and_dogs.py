def read(file_list):
    """ファイルの中身を読み込む"""
    try:
        with open(file_list, encoding='utf-8') as fl:
            content = fl.read()
    except FileNotFoundError:
        # print(f"{file_list}が見つかりません。")
        pass
    else:
        print(content)

file_dogs = 'dogs.txt'
file_cats = 'cats.txt'

file_lists = [file_dogs, file_cats]
for file_list in file_lists:
    read(file_list)
