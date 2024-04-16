filename = 'learning_python.txt'

# 一回目：ファイル全体を一度に読み込んで出力
with open(filename,encoding="utf-8_sig") as file_object:
    content = file_object.read()
    print(content)

# 二回目：ファイルオブジェクトを使って行ごとに出力
with open(filename,encoding="utf-8_sig") as file_object:
    for line in file_object:
        print(line.rstrip())

# 三回目：リストに各行を格納して出力
with open(filename,encoding="utf-8_sig") as file_object:
    lines = file_object.readlines()
    print(lines)

