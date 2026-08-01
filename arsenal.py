"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Manages the collection, firing, movement, drawing, and removal
of laser projectiles used by the player's ship.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 08/09/26
"""

import pygame
from typing import TYPE_CHECKING

from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage all laser projectiles fired by the player's ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize an empty projectile group and store game settings."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update every laser and remove lasers that leave the screen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Remove lasers that have traveled beyond the right edge."""
        screen_rect = self.game.screen.get_rect()

        for bullet in self.arsenal.copy():
            if bullet.rect.left >= screen_rect.right:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw every active laser projectile."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Create a laser when the maximum projectile count allows it."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True

        return False