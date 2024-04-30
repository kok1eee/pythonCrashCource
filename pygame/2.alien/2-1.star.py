import sys
import pygame

from settings import Settings
from star import Star
from random import randint

class Starry_sky:
    """星空を表すクラス"""

    def __init__(self):
        """初期化"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.stars = pygame.sprite.Group()

        self._create_starry_sky()

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        """キーボードとマウスのイベントに対応する"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """キーを押すイベントに対応する"""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_starry_sky(self):
        "星空を作成する"
        # 1つの星を作成する
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # 画面に収まるエイリアンの列数を決定する
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * star_height)

        # 星空を作成する
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """星を1つ作成、列の中に配置する"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """画面上の画像を更新し、新しい画像に切り替える"""
        self.screen.fill(self.settings.bg_color)

        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ss = Starry_sky()
    ss.run_game()
