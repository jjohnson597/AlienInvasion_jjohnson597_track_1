"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Creates, updates, draws, and manages waves of alien enemies
that enter from the right side and travel toward the player's ship.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 07/26/2026
"""

import pygame

from alien import Alien


class AlienFleet:
    """Manage waves of alien enemies moving from right to left."""

    def __init__(self, game):
        """Initialize the alien group and create the first enemy wave."""
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.aliens = pygame.sprite.Group()

        # A negative direction moves the aliens toward the left.
        self.alien_direction = -1

        self.create_fleet()

    def create_fleet(self):
        """Create an alien formation near the right side of the screen."""
        self.aliens.empty()

        sample_alien = Alien(self, 0, 0)
        alien_width = sample_alien.rect.width
        alien_height = sample_alien.rect.height

        # Keep the aliens below the score and high-score display.
        top_margin = 100
        bottom_margin = 40

        vertical_spacing = alien_height * 2
        horizontal_spacing = alien_width * 2

        available_space_y = (
            self.settings.screen_height
            - top_margin
            - bottom_margin
        )

        number_rows = max(
            1,
            available_space_y // vertical_spacing
        )

        # Use a smaller formation so it enters from the right like a wave.
        number_columns = 4

        start_x = (
            self.settings.screen_width
            - alien_width
            - 30
        )

        for column_number in range(number_columns):
            for row_number in range(number_rows):
                self._create_alien(
                    column_number,
                    row_number,
                    start_x,
                    top_margin,
                    horizontal_spacing,
                    vertical_spacing
                )

    def _create_alien(
        self,
        column_number,
        row_number,
        start_x,
        top_margin,
        horizontal_spacing,
        vertical_spacing
    ):
        """Create one alien at its assigned wave position."""
        alien = Alien(self, 0, 0)

        alien.x = (
            start_x
            - column_number * horizontal_spacing
        )

        alien.y = (
            top_margin
            + row_number * vertical_spacing
        )

        alien.rect.x = int(alien.x)
        alien.rect.y = int(alien.y)

        self.aliens.add(alien)

    def update_fleet(self):
        """Move every alien continuously toward the left side."""
        self.aliens.update()

    def draw(self):
        """Draw every alien in the active wave."""
        for alien in self.aliens.sprites():
            alien.draw_alien()

    def check_collisions(self, bullets):
        """Return collisions between the player's lasers and aliens."""
        return pygame.sprite.groupcollide(
            bullets,
            self.aliens,
            True,
            True
        )

    def check_destroyed_status(self):
        """Return True when every alien in the wave is destroyed."""
        return len(self.aliens) == 0

    def check_fleet_left_edge(self):
        """Return True when an alien reaches the edge behind the ship."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= self.screen_rect.left:
                return True

        return False