import pygame

class Rocket:
    """ロケットを管理するクラス"""

    def __init__(self, ai_game):
        """ロケットを初期化し、開始時の位置を設定する"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.rocket_speed = 1.5
        # ロケットの画像を読み込み、サイズを取得する
        self.image = pygame.image.load('1.spaceship\images\ロケット.png')
        self.rect = self.image.get_rect()
        
        # ロケットを真ん中に配置する
        self.rect.center = self.screen_rect.center

        # 左右の移動フラグ
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

        # ロケットの水平位置の浮動小数点数を格納する
        self.x = float(self.rect.x)
        # ロケットの垂直位置の浮動小数点数を格納する
        self.y = float(self.rect.y)

    def update(self):
        """左右の移動フラグによってロケットの位置を更新する"""
        # ロケットのxの値を更新する
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
        # ロケットのyの値を更新する
        if self.moving_top and self.rect.top > 0:
            self.y -= self.rocket_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed

        # self.xからrectオブジェクトの位置を更新する
        self.rect.x = self.x
        # self.yからrectオブジェクトの位置を更新する
        self.rect.y = self.y

    def blitme(self):
        """ロケットを現在位置に描画する"""
        self.screen.blit(self.image, self.rect)