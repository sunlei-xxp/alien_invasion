import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize a screen for the game
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建 Play 按钮
    play_button = Button(ai_settings, screen, "Play")

    # Create a ship
    ship = Ship(ai_settings, screen)

    # Create a group for bullets
    bullets = Group()

    # Create a group of alien
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the game main loop
    while True:
        gf.check_events(ai_settings, screen, stats,
                        play_button, ship, aliens, bullets)

        if stats.game_active == True:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)


run_game()
