class Settings():
    """This class store all settings for this game project"""

    def __init__(self):
        """Define all initial setings for the game"""
        # Setting for screen
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Setting for ships
        self.ship_limit = 3

        # Setting for bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Setting for aliens
        self.fleet_drop_speed = 5

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随着游戏进行而变化的设置
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # fleet_direction: 1 means right; -1 means left
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
