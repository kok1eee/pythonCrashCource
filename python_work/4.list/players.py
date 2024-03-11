players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# スライスによるループ
players = ['charles','martina','michael','eli']

print("チームの最初の3人の選手です。")
for player in players[:3]:
  print(player.title())

# リストをコピーする
my_foods = ['ピザ','だんご','ケーキ']
friend_foods = my_foods[:]

my_foods.append('チョコレート')
friend_foods.append('アイスクリーム')

print("私が好きな食べ物")
print(my_foods)

print("\n友達が好きな食べ物")
print(friend_foods)

