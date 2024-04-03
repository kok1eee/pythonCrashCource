sandwich_orders = ['ham','cheese','tuna','tomato','lettuce']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"{sandwich}サンドイッチができました。！")

print(finished_sandwiches)
