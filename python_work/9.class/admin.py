from user import User
from privileges import Privileges

class Admin(User):
    """管理者の情報を表すクラス"""
    def __init__(self,first_name,last_name,gender,age):
        """親クラスの属性を初期化する"""
        super().__init__(first_name,last_name,gender,age)
        self.privileges = Privileges()