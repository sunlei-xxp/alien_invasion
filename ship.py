import pygame


class Ship():
    """This is a class for all ships"""

    def __init__(self, ai_settings, screen):
        # Initialize the ship and set it's location
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Transfer the type to allow keep float data in center
        self.center = float(self.rect.centerx)

        # Index of moving
        self.move_right = False
        self.move_left = False

    def update(self):
        """Follow index of moving to update the location of ship"""
        # Update .center instead of rect.centerx
        if (self.move_right) and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        if (self.move_left) and (self.rect.left > self.screen_rect.left):
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Show the ship in designed location - bottm center of screen"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Let the ship in middle of the screen"""
        self.center = self.screen_rect.centerx
