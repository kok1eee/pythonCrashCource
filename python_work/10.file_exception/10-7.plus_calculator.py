print("数字を二つ入力してください")

while True:
    first_number = input("一つ目の数字を入力してください")
    second_number = input("二つ目の数字を入力してください")

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        pass
    else:
        print(answer)
        break
