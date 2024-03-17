# エイリアンの色によって点数をifで分ける

alien_colors = ['緑','黄','赤']

alien_color = alien_colors[0]

if alien_color == '緑':
    print("緑のエイリアンを倒した。プレイヤーが5点を獲得した！")
elif alien_color == '黄':
    print("黄のエイリアンを倒した。プレイヤーが10点を獲得した！")
elif alien_color == '赤':
    print("赤のエイリアンを倒した。")


alien_color = alien_colors[1]

if alien_color == '緑':
    print("緑のエイリアンを倒した。プレイヤーが5点を獲得した！")
elif alien_color == '黄':
    print("黄のエイリアンを倒した。プレイヤーが10点を獲得した！")
elif alien_color == '赤':
    print("赤のエイリアンを倒した。プレイヤーが15点を獲得した！")


alien_color = alien_colors[2]

if alien_color == '緑':
    print("緑のエイリアンを倒した。プレイヤーが5点を獲得した！")
elif alien_color == '黄':
    print("黄のエイリアンを倒した。プレイヤーが10点を獲得した！")
elif alien_color == '赤':
    print("赤のエイリアンを倒した。プレイヤーが15点を獲得した！")


# 年齢によって表示を変更する
family =[31,33,3,1]

family_age = family[0]

if family_age < 2:
    print("あなたは赤ちゃんです。")
elif family_age < 4:
    print("あなたは幼児です。")
elif family_age < 13:
    print("あなたは子供です。")
elif family_age < 20:
    print("あなたはティーンエイジャーです。")
elif family_age < 65:
    print("あなたは大人です。")
elif family_age >= 65:
    print("あなたは高齢者です。")

# 好きな果物
favorite_fruits = ['apple','banana','strawberry']

if 'kiwi' in favorite_fruits:
    print("あなたはkiwiが本当に好きですね！")
if 'pear' in favorite_fruits:
    print("あなたはpearが本当に好きですね！")
if 'peach' in favorite_fruits:
    print("あなたはpeachが本当に好きですね！")
if 'banana' in favorite_fruits:
    print("あなたはbananaが本当に好きですね！")
