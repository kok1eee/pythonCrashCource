def count_words(filename):
    """ファイルに含まれる大体の単語の数を数える"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"ごめんなさい。{filename}は見当たりません。")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"ファイル{filename}には約{num_words}の単語が含まれます。")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)