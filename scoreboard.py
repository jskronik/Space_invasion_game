import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Class created to present scoring information"""

    def __init__(self, ai_settings, screen, stats):
        """Initialization of scoring attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font options for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/space_age.ttf', 26)

        # Preparation of initial scoring image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Converting a score into a generated image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = 'SCORE: ' + '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display of scores in the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displaying the scores on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """conversion of the best score in the game to the screen"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = 'HIGH SCORE: ' + '{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the best score in the game in the middle of the screen at the top edge
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Conversion of the level number to the screen"""
        level_str = 'LEVEL: ' + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)
        # The number of level is displayed under the current scoreboard
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Display the number of ships, which user still have"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
