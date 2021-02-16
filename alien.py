import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class for single alien"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the image of alien, and set attribute 'rect'
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Each new alien is at top-left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the accurate position of alien
        self.x = float(self.rect.x)

    def blit_me(self):
        """Draw the alien at top-left"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """If alien arrives to edge, then return 'True' """
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True
        if self.rect.left < 0:
            return True

    def update(self):
        """Move aliens to right/ or left"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
