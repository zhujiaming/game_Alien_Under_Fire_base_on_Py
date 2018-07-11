class Settings:
    def __init__(self):
        self.title = "外星人入侵"
        self.screen_width = 512
        self.screen_height = 512
        self.bg_color = (230, 230, 230)
        #  飞船的设置
        self.ship_speed_factor = 0.7

        # 子弹设置
        self.bullet_speed_factor = 0.25
        self.bullet_width = 220
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #  外星人设置
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 5
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1
