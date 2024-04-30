import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """星を表すクラス"""
    def __init__(self, ss):
        super().__init__()
        self.screen = ss.screen
        
        # 星の画像を読み込み、サイズを取得する
        self.image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # 星を画面の左上の近くに配置する
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # エイリアンの実際の位置を格納する
        self.x = float(self.rect.x)
