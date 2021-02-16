class GameStats():
    """This is a class to keep game statistic info"""

    def __init__(self, ai_settings):
        """Initialize the statistic info"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # game_active is True when initialize
        self.game_active = True

    def reset_stats(self):
        """Intialize the statistics which may change during game"""
        self.ship_left = self.ai_settings.ship_limit
