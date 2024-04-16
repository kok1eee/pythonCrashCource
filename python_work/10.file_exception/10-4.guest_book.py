filename = 'guest_book.txt'

while True:
    name = input("あなたの名前を教えてください。")

    if name == '終了':
        break
    else:
        with open(filename, 'a', encoding='utf-8_sig') as file_object:
            file_object.write(f"{name}様\n")

