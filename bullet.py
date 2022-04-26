import random
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class created for managing bullets fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
        """Creating bullet object at the current ship position"""
        super().__init__()
        self.screen = screen

        # Creating rectangular bullet in point(0,0) and then defining proper position for it
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # The bullet position is defined by a float value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moving the bullet on the screen"""
        # Update the bullet position
        self.y -= self.speed_factor
        # Update the rectangle bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Alien_bullet(Sprite):
    """Class created for managing bullets fired from the aliens"""
    def __init__(self, ai_settings, screen, aliens):
        """Creating alien bullet object at the current alien position"""
        super().__init__()
        self.screen = screen

        # Creating rectangular bullet in point(0,0) and then defining proper position for it
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_alien_width, ai_settings.bullet_alien_height)
        enemies = []
        for alien in aliens:
            enemies.append(alien)
            alien = random.choice(enemies)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        # The bullet position is defined by a float value
        self.y = float(self.rect.y)

        self.color = ai_settings.alien_bullet_color
        self.speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        """Moving the bullet on the screen"""
        # Update the alien bullet position
        self.y += self.speed_factor
        # Update the rectangle bullet position
        self.rect.y = self.y

    def draw_alien_bullet(self):
        """Displaying alien bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)