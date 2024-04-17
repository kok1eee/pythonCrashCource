import json

favorite_number = int(input("好きな数字を入れてください"))

filename = 'favorite_number.json'

with open(filename,'w') as f:
    json.dump(favorite_number, f)

