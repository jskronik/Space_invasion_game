import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # Game initialization, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, 'Start game')
    # Create a ship, aliens and bullets
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Game Statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Loading the highest score
    gf.load_score(stats)
    sb.prep_high_score()

    # Starting the main loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            alien_bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_alien_bullets(ai_settings, alien_bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, alien_bullets)


run_game()

