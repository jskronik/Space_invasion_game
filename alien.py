import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing single alien in alien fleet"""
    def __init__(self, ai_settings, screen):
        """Alien inicialization and defining its initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading an alien image and defining its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Placing a new alien near the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact position of the alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True value if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    def update(self):
        """Moving alien into right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Displaying alien in its actual position"""
        self.screen.blit(self.image, self.rect)