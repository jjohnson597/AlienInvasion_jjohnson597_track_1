"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Defines the horizontal laser projectiles fired by the player's ship.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 07/26/2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represent a laser fired horizontally by the player's ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Create a laser at the right side of the player's ship."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
        self.settings.bullet_file
)

        self.image = pygame.transform.rotate(
            self.image,
            -90
        )

        self.image = pygame.transform.scale(
            self.image,
    (
        self.settings.bullet_width,
        self.settings.bullet_height
    )
)

        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the laser horizontally toward the right side."""
        self.x += self.settings.bullet_speed
        self.rect.x = int(self.x)

    def draw_bullet(self):
        """Draw the laser at its current position."""
        self.screen.blit(self.image, self.rect)