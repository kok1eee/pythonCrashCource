def make_album(artist,album_title,number=""):
    """アーティスト名とアルバム名を受け取り、辞書にして返す"""
    if number:
        album = {'name':artist,'title':album_title,'song':number}
    else:
        album = {'name':artist,'title':album_title}
    return album
    
album_1 = make_album('BUMP','yggdrasil',17)
album_2 = make_album('宇多田ヒカル','Automatic',2)
album_3 = make_album('ポルノグラフィティ','アポロ',10)

album_list = [album_1,album_2,album_3]
print(album_list)
