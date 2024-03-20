request_topping = 'マッシュルーム'

if request_topping != 'アンチョビ':
  print("アンチョビを注文してください！")

request_toppings = ['マッシュルーム','エクストラチーズ']

if 'マッシュルーム' in request_toppings:
  print("マッシュルームを追加する。")
if 'ペパロニ' in request_toppings:
  print("ペパロニを追加する。")
if 'エクストラチーズ' in request_toppings:
  print("エクストラチーズを追加する。")

print("\nピザができました！")

requested_toppings = ['マッシュルーム','ピーマン','エクストラチーズ']

for requested_topping in requested_toppings:
  print(f"ピザに{requested_topping}を追加します。")
print("\nピザができました！")

for requested_topping in requested_toppings:
  if requested_topping == 'ピーマン':
    print("申し訳ありません、ピーマンは品切れです。")
  else:
    print(f"ピザに{requested_topping}を追加します。")

print("\nピザができました！")

requested_toppings = []

if requested_toppings:
  for requested_topping in requested_toppings:
    print(f"トッピングに{requested_topping}を追加します。")
  print("\nピザができました。")
else:
  print("\nプレーンピザでよろしいですか？")

available_toppings = ['マッシュルーム','オリーブ','ピーマン','ペパロニ','パイナップル','エクストラチーズ']

requested_toppings = ['マッシュルーム','フライドポテト','エクストラチーズ']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"ピザに{requested_topping}を追加します。")
  else:
    print(f"申し訳ございません、{requested_topping}はありません。")

print("ピザができました。")