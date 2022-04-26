import pygame.image
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings,screen):
        """Initialization of the spacecraft and its initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading the ship's image and retrieving its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Loading a ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # The ship center point is stored as a float number
        self.center = float(self.rect.centerx)

        # Options indicating the movement of the ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship positions based on the option indicating its movement"""
        # Update the value of the ship center point, not its rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update of rect object based on self.center value
        self.rect.centerx = self.center

    def blitme(self):
        """Display of the spacecraft in its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Placing the ship in the middle at the bottom edge of the screen"""
        self.center = self.screen_rect.centerx
