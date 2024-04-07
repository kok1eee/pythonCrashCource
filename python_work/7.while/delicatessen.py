sandwich_orders = ['pastrami','ham','cheese','pastrami','tuna','tomato','pastrami','lettuce']
finished_sandwiches = []

print('パストラミサンドは売り切れです。')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"{sandwich}サンドイッチができました。！")

print(finished_sandwiches)

