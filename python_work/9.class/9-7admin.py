class User:
    """first_nameとlast_nameといくつかの必要情報の属性を作成"""
    def __init__(self,first_name,last_name,gender,age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}さんは{self.age}の{self.gender}性です")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name}さんこんにちは！いい天気ですね！")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name} {self.last_name}さんのログイン回数は{self.login_attempts}回です。")

    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"{self.first_name} {self.last_name}さんのログイン回数は0回です。")

class Privileges:
    def __init__(self,privileges=['投稿を追加する','投稿を削除する','ユーザーを利用禁止にする']):
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges

class Admin(User):
    """管理者の情報を表すクラス"""
    def __init__(self,first_name,last_name,gender,age):
        """親クラスの属性を初期化する"""
        super().__init__(first_name,last_name,gender,age)
        self.privileges = Privileges()

admin_user = Admin('masayoshi','tazawa','man',31)
print(f"{admin_user.first_name} {admin_user.last_name}の持っている権限は{admin_user.privileges.show_privileges()}")