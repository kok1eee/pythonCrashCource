def make_album(artist,album_title,number=""):
    """アーティスト名とアルバム名を受け取り、辞書にして返す"""
    if number:
        album = {'name':artist,'title':album_title,'song':number}
    else:
        album = {'name':artist,'title':album_title}
    return album

while True:
    print("あなたの好きなアルバムを教えてください")
    print("各項目で'終了'を入力すると終わります。")

    artist = input("アーティストの名前を教えてください。")
    if artist == '終了':
        break

    album_title = input("タイトルを教えてください。")
    if album_title == '終了':
        break

    number = input("曲数は何曲ありますか？わからなければ飛ばしてください。")
    if number == '終了':
        break

    album_date = make_album(artist,album_title,number)
    print(album_date)
