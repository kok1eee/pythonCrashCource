class Restaurant:
    """レストラン名と料理の種類を格納"""
    def __init__(self,name,kind):
        """レストラン名と料理の種類属性を初期化する"""
        self.name = name
        self.kind = kind
        # デフォルト値が0のnumber_servedという属性を追加。
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"\n{self.name}は{self.kind}のお店です。")

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

shop1 = Restaurant('田中商店','ラーメン')
shop2 = Restaurant('サイゼリヤ','高級イタリアン')
shop3 = Restaurant('すきや','チー牛')

shop1.describe_restaurant()
shop2.describe_restaurant()
shop3.describe_restaurant()

shop1.update_set_number_served(1_000)

shop1.increment_number_served(5_000)

shop1.set_number_served()

