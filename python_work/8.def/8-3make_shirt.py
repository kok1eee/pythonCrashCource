# def make_shirt():
#     """Tシャツのサイズとプリントするメッセージについての文章を出力"""
#     size = input("サイズを入力してください。S/M/L")
#     message = input("プリントするメッセージを入力してください。")
#     print(f"サイズは{size}でプリントするメッセージは{message}です。")

# make_shirt()

def make_shirt(size='L',message='I LOVE Python'):
    """Tシャツのサイズとプリントするメッセージについての文章を出力"""
    print(f"サイズは{size}でプリントするメッセージは{message}です。")

# make_shirt('S','O')

make_shirt()
make_shirt(size='M')
make_shirt(size='XXL',message='月曜日でしごとやめる')