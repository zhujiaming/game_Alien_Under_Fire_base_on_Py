class Settings:
    def __init__(self):
        self.title = "外星人入侵"
        self.screen_width = 1024
        self.screen_height = 512
        self.bg_color = (230, 230, 230)
        #  飞船的设置
        self.ship_speed_factor = 0.7
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 0.25
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #  外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 20
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1

        #  以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #  外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def add_alien_speed(self, num):
        temp_alien_speed_factor = round(self.alien_speed_factor + num, 2)  # 有精度溢出的问题
        if temp_alien_speed_factor < 0:
            temp_alien_speed_factor = 0
        elif temp_alien_speed_factor > 1:
            temp_alien_speed_factor = 1
        self.alien_speed_factor = temp_alien_speed_factor

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 0.25
        self.alien_speed_factor = 0.1
        # fleet_direction 为 1 表示向右；为 -1 表示向左
        self.fleet_direction = 1
        #  记分
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度设置和外星人点数 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
