import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """action for if keydown event"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    # Create a bullet and add it in group of bulliets,
    # bullet no more than max allowed qty
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """action for if keyup event"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """check the keyboard and mouse events and response"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,
                              play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        #  重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人,并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship,  aliens, bullets, play_button):
    """update the image in screen and refresh it"""
    # Fill the screen with background color in every loop
    screen.fill(ai_settings.bg_color)

    # Fresh all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Show the ship
    ship.blitme()

    # Show the alien
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态,就绘制Play 按钮
    if not stats.game_active:
        play_button.draw_button()

    # Show the screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update bullets location and remove the bullet disappeard"""
    # Update bullet location
    bullets.update()

    # Remove bullets out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # print(len(bullets))  # use this to check the length of bullets
    check_bullets_aliens_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullets_aliens_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Check if any collide of bullet & alien
    # If Yes, remove the alien and bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score

    if len(aliens) == 0:
        # Remove bullets, 加快游戏节奏, and create a new group of alien
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculate the number of aliens in a column"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculate how many rows of aliens can be keep in screen"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create a alien and put it in current column"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # Create a fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create a new alien and add it in fleet
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """if alien arrives to edge, take actions"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Move aliens down and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Actions if a ship is hit"""
    if stats.ship_left > 0:

        # ship_left minus 1
        stats.ship_left -= 1

        # Clean all aliens and bullets group
        aliens.empty()
        bullets.empty()

        # Create a new group of aliens and a new ship in bottom center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Sleep for 0.5s
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any alien arrive to bottom edge of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Same action as ship is hitted
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Check edge and Update location of all aliens in group of aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check if alien collide with the ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Check if any alien arrive to bootm edge of screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
