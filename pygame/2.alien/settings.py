class Settings:
    """エイリアン侵略の全設定を格納するクラス"""

    def __init__(self):
        """ゲームの初期設定"""
        # 画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 宇宙船の設定
        self.ship_speed = 1.5

        # 弾の設定
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 横打ちの弾の設定

        self.h_bullet_width = 15
        self.h_bullet_height = 3

        # エイリアンの設定
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 艦隊の移動方向を表し1は右、-1は左に移動することを表す
        self.fleet_direction = 1

