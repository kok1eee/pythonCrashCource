for value in range(1,21):
  print(value)

# 1から1000000まで
million = list(range(1,1000001))

print(min(million))
print(max(million))
print(sum(million))

million = []

for value in range(1,1000001):
  million.append(value)
print(min(million))
print(max(million))
print(sum(million))

# 奇数
odd = []
for value in range(1,20,2):
  odd.append(value)
print(odd)

# 3の倍数
three = []
for value in range(3,30,3):
  three.append(value)
print(three)


# 立方数

cube = []

for value in range(1,11):
  cube.append(value**3)
print(cube)

cube = [value**3 for value in range(1,11)]
print(cube)