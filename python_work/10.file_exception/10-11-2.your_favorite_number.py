import json

filename = 'favorite_number.json'

with open(filename, 'r') as f:
    numbers = json.load(f)

print(f"あなたの好きな数字を知っています！それは{numbers}です。")