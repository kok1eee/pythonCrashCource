class Privileges:
    def __init__(self,privileges=['投稿を追加する','投稿を削除する','ユーザーを利用禁止にする']):
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges