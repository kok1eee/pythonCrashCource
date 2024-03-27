rivers = {
    'arakawa':'japan',
    'nile':'egypt',
    'amazon':'south_america',
    'mississippi':'america',
    'yangtze':'china'
    }

for river,country in rivers.items():
    print(f"{river.title()}は{country.title()}にあります。")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
