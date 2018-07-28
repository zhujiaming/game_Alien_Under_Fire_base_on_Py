import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption(ai_settings.title)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    #  创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    stats = GameStats(ai_settings)

    play_button = Button(ai_settings, screen, "START")
    #  创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb)
            gf.update_aliens(ai_settings, screen, ship, aliens, bullets, stats, sb)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)


run_game()
