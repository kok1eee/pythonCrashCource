class Employee:
    """従業員の情報を表示する"""

    def __init__(self, first, last, income):
        """初期化する"""
        self.first = first
        self.last = last
        self.income = income
    
    def information(self):
        """情報の表示"""
        full_name = f"{self.first} {self.last}"
        info = f"私の名前は{full_name.title()}で年収は{self.income}です。"
        return info
    
    def give_raise(self,number=""):
        """昇給額を引数で指定した額をあげる、またはデフォルトで500000円をあげる"""
        if number:
            self.income += number
        else:
            self.income += 500_000