"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Defines the player's ship, vertical movement, laser firing,
drawing behavior, and collision detection.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 08/09/26
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """Represent the player-controlled ship in the side-scrolling game."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship, position it on the left, and attach its arsenal."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.ship_width,
                self.settings.ship_height
            )
        )
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        self.rect.x += 20

        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.arsenal = arsenal

    def update(self):
        """Update the ship's movement and all active lasers."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Move the ship vertically while keeping it within the screen."""
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = int(self.y)

    def draw(self):
        """Draw the active lasers and the player's ship."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Attempt to fire a laser and return whether one was created."""
        return self.arsenal.fire_bullet()

    def check_collisions(self, alien_group):
        """Return the alien colliding with the ship, or None."""
        return pygame.sprite.spritecollideany(
            self,
            alien_group
        )