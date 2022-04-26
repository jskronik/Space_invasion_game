class Settings():
    """Class designed to capture all game settings"""
    def __init__(self):
        """Initialization of game settings"""
        # Screen settings
        self.screen_width = 1150
        self.screen_height = 750
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 0.4
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 8
        self.bullet_height = 12
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3
        self.bullet_alien_width = 3
        self.bullet_alien_height = 5
        self.alien_bullets_allowed = 5
        self.alien_bullet_color = (255, 0, 0)

        # Alien settings
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_points = 50

        # Game speed change
        self.speedup_scale = 1.06
        self.speedup_ship = 1.03
        self.speedup_bullet = 1.03
        self.initialize_dynamic_settings()

        # Score increase factor
        self.score_scale = 1.2

    def initialize_dynamic_settings(self):
        """Initialization of settings which are changed during the game"""
        self.ship_speed_factor = 0.4
        self.bullet_speed_factor = 0.4
        self.alien_speed_factor = 0.2
        self.fleet_direction = 1
        self.alien_bullet_speed_factor = 0.055

    def increase_speed(self):
        """Changing the speed settings"""
        self.ship_speed_factor *= self.speedup_ship
        self.bullet_speed_factor *= self.speedup_bullet
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)