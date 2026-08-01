"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Creates, updates, draws, and manages changing alien formations
that enter from the right side and travel toward the player's ship.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 08/09/2026
"""

import pygame

from alien import Alien


class AlienFleet:
    """Manage level-based alien waves moving from right to left."""

    def __init__(self, game):
        """Initialize the alien group and create the first enemy wave."""
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.aliens = pygame.sprite.Group()

        # A negative direction moves aliens toward the player's side.
        self.alien_direction = -1
        self.formation_name = "rectangle"

        self.create_fleet()

    def create_fleet(self):
        """Create a formation selected according to the current level."""
        self.aliens.empty()

        sample_alien = Alien(self, 0, 0)
        alien_width = sample_alien.rect.width
        alien_height = sample_alien.rect.height

        formation_points = self._get_formation_points()

        horizontal_spacing = alien_width * 2
        vertical_spacing = alien_height * 2

        start_x = (
            self.settings.screen_width
            - alien_width
            - 30
        )

        top_margin = 100
        bottom_margin = 40
        available_height = (
            self.settings.screen_height
            - top_margin
            - bottom_margin
        )

        highest_row = max(
            row_number
            for _, row_number in formation_points
        )

        formation_height = (
            highest_row + 1
        ) * vertical_spacing

        start_y = (
            top_margin
            + max(
                0,
                (available_height - formation_height) // 2
            )
        )

        for column_number, row_number in formation_points:
            self._create_alien(
                column_number,
                row_number,
                start_x,
                start_y,
                horizontal_spacing,
                vertical_spacing
            )

    def _get_formation_points(self):
        """Return coordinate points for the current level's formation."""
        level = self.game.game_stats.level

        formation_number = (level - 1) % 5

        if formation_number == 0:
            self.formation_name = "rectangle"
            return self._rectangle_formation()

        if formation_number == 1:
            self.formation_name = "wedge"
            return self._wedge_formation()

        if formation_number == 2:
            self.formation_name = "diamond"
            return self._diamond_formation()

        if formation_number == 3:
            self.formation_name = "zigzag"
            return self._zigzag_formation()

        self.formation_name = "split_columns"
        return self._split_column_formation()

    def _rectangle_formation(self):
        """Return points for a compact rectangular fleet."""
        return [
            (column, row)
            for column in range(3)
            for row in range(5)
        ]

    def _wedge_formation(self):
        """Return points for a wedge-shaped fleet."""
        return [
            (0, 2),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4)
        ]

    def _diamond_formation(self):
        """Return points for a diamond-shaped fleet."""
        return [
            (0, 2),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (3, 1),
            (3, 2),
            (3, 3),
            (4, 2)
        ]

    def _zigzag_formation(self):
        """Return points for an angled zigzag fleet."""
        return [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 3),
            (6, 2),
            (7, 1)
        ]

    def _split_column_formation(self):
        """Return points for two separated enemy columns."""
        return [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4)
        ]

    def _create_alien(
        self,
        column_number,
        row_number,
        start_x,
        start_y,
        horizontal_spacing,
        vertical_spacing
    ):
        """Create one alien at its assigned formation position."""
        alien = Alien(self, 0, 0)

        alien.x = (
            start_x
            - column_number * horizontal_spacing
        )

        alien.y = (
            start_y
            + row_number * vertical_spacing
        )

        alien.rect.x = int(alien.x)
        alien.rect.y = int(alien.y)

        self.aliens.add(alien)

    def update_fleet(self):
        """Move every alien in the active formation."""
        self.aliens.update()

    def draw(self):
        """Draw every alien in the active wave."""
        for alien in self.aliens.sprites():
            alien.draw_alien()

    def check_collisions(self, bullets):
        """Destroy no more than one alien for each laser."""
        collisions = {}

        for bullet in bullets.sprites():
            aliens_hit = pygame.sprite.spritecollide(
                bullet,
                self.aliens,
                False
            )

            if aliens_hit:
                alien_hit = aliens_hit[0]

                bullet.kill()
                alien_hit.kill()

                collisions[bullet] = [alien_hit]

        return collisions

    def check_destroyed_status(self):
        """Return True when every alien in the wave is destroyed."""
        return len(self.aliens) == 0

    def check_fleet_left_edge(self):
        """Return True when an alien reaches the edge behind the ship."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= self.screen_rect.left:
                return True

        return False