favorite_places = {'masayoshi':['beer_ma','beer_boy'],'mina':'chiba','divina':'philippines'}

for name,place in favorite_places.items():
    print(f"{name}の好きな場所は{place}です。")

for name in favorite_places.keys():
    f_place = favorite_places[name]
    print(f"{name}の好きな場所は{f_place}です。")

for place in favorite_places.values():
    print(f"私の好きな場所は{place}です。")