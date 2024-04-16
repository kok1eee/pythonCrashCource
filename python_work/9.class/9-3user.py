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



person1 = User('masayoshi','tazawa','男',31)
person2 = User('kazunari','sato','男',24)

person1.describe_user()
person2.describe_user()

person1.greet_user()
person2.greet_user()

person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person2.increment_login_attempts()

person1.reset_login_attempts()

person2.increment_login_attempts()
