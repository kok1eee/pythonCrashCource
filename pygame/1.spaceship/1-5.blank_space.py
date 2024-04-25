import sys
import pygame

class blank_space:
    """空白の画面用のクラス"""

    def __init__(self):
        """初期設定"""
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        
        self.bg_color = (0, 0, 0)
        
    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

    def _check_events(self):
        """キーボードとマウスのイベントに対応する"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(f"押されたキー = {pygame.key.name(event.key)}")

bs = blank_space()
bs.run_game()
