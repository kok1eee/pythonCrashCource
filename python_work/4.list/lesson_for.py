pizzas = ['マルゲリータ','ペパロニ','マリナーラ','ペスカトーレ']

for pizza in pizzas:
  print(f"\n私は{pizza}ピザが好きです。")
print("誕生日に食べるピザがたまらなく好きです！")

friend_pizzas = pizzas[:]

pizzas.append('トロピカル')

friend_pizzas.append('スパイシー')

print(pizzas)
print(friend_pizzas)

for pizza in pizzas[:2]:
  print(pizza)

animals = ['犬','ネコ','たぬき','きつね']

for animal in animals:
  print(f"\n{animal}は素晴らしいペットです。")
print("この動物たちはとても素晴らしいペットです！")