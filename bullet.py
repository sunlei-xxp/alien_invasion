import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class for bullet released from ship, it's heritate from class pygame.sprite.Sprite"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the location of ship, with bullet settings"""
        super().__init__()
        self.screen = screen

        # Create a bullet at (0,0) and then set it at right position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the y position of bullet in a float data
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Method to move the bullet upwards"""
        # Update the float data of bullet y position
        self.y -= self.speed_factor
        # Update the y data for bullet.rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
