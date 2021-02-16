class Settings():
    """This class store all settings for this game project"""

    def __init__(self):
        """Define all initial setings for the game"""
        # Setting for screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Setting for ships
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Setting for bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Setting for aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction: 1 means right; -1 means left
        self.fleet_direction = 1
