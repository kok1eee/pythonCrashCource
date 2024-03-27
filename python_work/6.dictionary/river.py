rivers = {
    'arakawa':'japan',
    'nile':'egypt',
    'amazon':'south_america',
    'mississippi':'america',
    'yangtze':'china'
    }
for river, country in rivers.items():
    print(f"{river}は{country}を流れている")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
