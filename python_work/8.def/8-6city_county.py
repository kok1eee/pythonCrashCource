def city_country(city,country):
    """フォーマットされた文字列を返します"""
    responses = f"{city},{country}"
    return responses.title()

while True:
    print("\nあなたのいきたい町と国を教えてください。")
    print("'終了'を入力すると終了します。")

    city = input("行きたい町の名前を教えてください")
    if city == '終了':
        break

    country = input("その町はどこの国にありますか？")
    if country == '終了':
        break

    formatted_response = city_country(city,country)
    print(f"{formatted_response}")