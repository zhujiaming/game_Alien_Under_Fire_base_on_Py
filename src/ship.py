import pygame
from setting import Settings
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.setting = Settings()
        self.screen = screen
        self.isMovingRight = False
        self.isMovingLeft = False

        # 加载飞船并获取其外接矩形
        self.image = pygame.image.load('image/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.center < self.setting.screen_width:
            self.center += self.setting.ship_speed_factor
        if self.moving_left and self.center > 0:
            self.center -= self.setting.ship_speed_factor

        #  根据 self.center 更新 rect 对象
        self.rect.centerx = self.center

    def center_ship(self):
        """ 让飞船在屏幕上居中 """
        self.center = self.screen_rect.centerx
