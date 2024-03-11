#個人的なメッセージ
name = "Eric"
print(f"こんにちは{name}、今日はPythonを学びますか？")

#名前の大文字小文字
first_name = "emma"
last_name = "watson"
print(f"{first_name.lower()} {last_name.lower()}")
print(f"{first_name.upper()} {last_name.upper()}")
print(f"{first_name.title()} {last_name.title()}")

#名言の引用
print('ドリー・パートンは"虹を見たかったら、雨も我慢しなくちゃね"と言った。')

#名言の引用2
famous_person = "ドリー・パートン"
message = f'{famous_person}は"虹を見たかったら、雨も我慢しなくちゃね"と言った。'
print(message)

#名前から空白を取り除く
my_name = "\nmasayoshi tazawa\n\t"
print(my_name)
print(my_name.lstrip())
print(my_name.rstrip())
print(my_name.strip())