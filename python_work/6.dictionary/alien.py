# alien_0 = {'color':'green','points':5}

# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"{new_points}点獲得しました！")

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(f"エイリアンは{alien_0['color']}です。")

alien_0['color'] = 'yellow'
print(f"エイリアンは{alien_0['color']}になりました。")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(f"最初のX座標:{alien_0['x_position']}")

# エイリアンは右に移動します。
# 現在のスピードによってエイリアンの移動距離を決定します。

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 素早いエイリアン
    x_increment = 3

# 新しい位置は元の位置に移動距離を加算します。
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"新しいX座標:{alien_0['x_position']}")

alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


# エイリアンを格納する空のリストを作成する

aliens = []

# 30匹のエイリアンを生成する
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 最初の5匹のエイリアンの情報を出力する
for alien in aliens[:5]:
    print(alien)
print("...")

# 生成されたエイリアンの数を出力する
print(f"全エイリアンの数:{len(aliens)}")