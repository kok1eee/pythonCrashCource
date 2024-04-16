def count_words(filename):
    """ファイルの中の単語が何回登場するか数える"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ごめんなさい。{filename}は見当たりません。")
    else:
        num = content.count('the ')
        print(f"{filename}にはtheが約{num}回登場します。")


filename = 'botanist_repository.txt'
count_words(filename)
