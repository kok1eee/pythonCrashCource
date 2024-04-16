filename = 'learning_python.txt'

# with open(filename,encoding="utf-8_sig") as file_object:
#     lines = file_object.readlines()
#     print(lines)

#     # 'Python'を'C言語'に置換
#     lines = [line.replace('Python', 'C言語') for line in lines]
#     print(lines)


with open(filename,encoding="utf-8_sig") as file_object:
    for line in file_object:
        print(line.replace('Python','C言語').rstrip())
