class Restaurant:
    """レストラン名と料理の種類を格納"""
    def __init__(self,name,kind):
        """レストラン名と料理の種類属性を初期化する"""
        self.name = name
        self.kind = kind
        # デフォルト値が0のnumber_servedという属性を追加。
        self.number_served = 0
    
    def describe_restaurant(self):
        message = f"\n{self.name}は{self.kind}のお店です。"
        return message

    def open_restaurant(self):
        print(f"\nレストラン開店情報です。\n{self.kind}の{self.name}というお店がオープンしました。")

    def set_number_served(self):
        """本日何人の来店があったか出力します。"""
        print(f"{self.name}に今日は{self.number_served}人きました。")

    def update_set_number_served(self,number):
        """指定された値に人数を更新する"""
        self.number_served = number
    
    def increment_number_served(self,number):
        if number > 0:
            self.number_served += number
        else:
            print("人数は減らせません。")
