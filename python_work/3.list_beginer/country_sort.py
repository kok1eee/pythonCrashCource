#行きたい国5個

country = ['usa','canada','philippine','norway','germany']
print(country)

# sorted()関数を使ってソート
print(sorted(country))

# リストの順番が変わっていないか確認
print(country)

# リスト逆順にソートともう一度逆順にソート
country.reverse()
print(country)

country.reverse()
print(country)

# リストをアルファベット順にソートとアルファベットの逆順にソート
country.sort()
print(country)

country.sort(reverse=True)
print(country)
