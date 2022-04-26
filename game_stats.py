class GameStats():
    def __init__(self, ai_settings):
        """Game statistics initialization"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0
        # Starting the game in the inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialization of statistical data that may change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0