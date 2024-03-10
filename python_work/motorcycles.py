motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#poped_motorcycles = motorcycles.pop()
print(motorcycles)
#print(poped_motorcycles)

last_owned = motorcycles.pop()
print(f"最近手に入れたバイクは{last_owned.title()}です。")

first_owned = motorcycles.pop(0)
print(f"最初に手にいれたバイクは{first_owned.title()}です。")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}は私には高すぎます。")

