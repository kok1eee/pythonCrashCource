guest = ['totsuka','fujimoto','hisakawa',]

message_1 = f"{guest[0]}様、未来は誰かに変えてもらうのではなく自分で変えるものだと知りました"
message_2 = f"{guest[1]}様、一番なりたい上司の像でした"
message_3 = f"{guest[2]}様、ラウンドワンの社員になるきっかけをいただいてありがとうございました。"

print(message_1)
print(message_2)
print(message_3)

#hisakawa様が参加できなくなったのでhoshino様を招待

absence = "hisakawa"
guest.remove(absence)
guest.append('hoshino')

message_3 = f"{guest[2]}様、ビジネスマンとして非常に勉強になりました。"

print(message_3)
print(f"今回の欠席者は{absence}様です。")

#大きいテーブルを見つけたので新しく三人招待

print("大きなテーブルを見つけました！")

guest.insert(0,'goto')
guest.insert(2,'iwasaki')
guest.append('miyazawa')

message_1 = f"{guest[0]}様、結婚式のスピーチありがとうございました。"
message_2 = f"{guest[1]}様、未来は誰かに変えてもらうのではなく自分で変えるものだと知りました"
message_3 = f"{guest[2]}様、一番応援していたアイドルでした。"
message_4 = f"{guest[3]}様、一番なりたい上司の像でした"
message_5 = f"{guest[4]}様、ビジネスマンとして非常に勉強になりました。"
message_6 = f"{guest[5]}様、人生が狂いました"

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)

#大きなテーブルが夕食の時間に間に合わないことが分かったため、一人減らさないといけない
print("夕食には二人しか招待できません")

apology = "様、大変申し訳ございません。手違いにより招待できなくなってしまいました"
pleasure = "様、会えるのを楽しみにしております。"
list_number = len(guest)

# リストの数が2になるまで数を減らす
while list_number > 2:
  popped_guest = guest.pop()
  print(f"{popped_guest}{apology}")
  list_number = len(guest)

# 残った人に招待メッセージ
print(f"{guest[0]}{pleasure}")
print(f"{guest[1]}{pleasure}")

# 残ったリストを削除
del guest[1]
del guest[0]

print(guest)