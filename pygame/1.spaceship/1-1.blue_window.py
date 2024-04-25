import sys
import pygame

from rocket import Rocket

class Bluesky:
    """青い空のためのクラス"""

    def __init__(self):
        """初期設定"""
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        
        self.bg_color = (0, 0, 255)

        self.rocket = Rocket(self)

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            
            self._check_events()
            self.rocket.update()
            self.screen.fill(self.bg_color)
            self.rocket.blitme()

            pygame.display.flip()
    
    def _check_events(self):
        """キーボードとマウスのイベントに対応する"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """キーを押すイベントに対応する"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """キーを離すイベントに対応する"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = False
    
    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
    
if __name__ == '__main__':
    # ゲームのインスタンスを作成し、ゲームを実行する
    ai = Bluesky()
    ai.run_game()