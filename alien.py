"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Defines an individual alien, including its image, position,
horizontal movement, edge detection, and drawing behavior.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 08/09/26
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Represent one alien belonging to the alien fleet."""

    def __init__(
        self,
        fleet: "AlienFleet",
        x: float,
        y: float
    ):
        """Initialize the alien at the supplied screen coordinates."""
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.game.settings
        self.boundaries = fleet.game.screen.get_rect()

        self.image = pygame.image.load(
            self.settings.alien_file
        )

        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.alien_width,
                self.settings.alien_height
            )
        )
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien horizontally in the fleet's current direction."""
        self.x += (
            self.settings.alien_speed
            * self.fleet.alien_direction
        )

        self.rect.x = int(self.x)

    def check_edges(self):
        """Return True when the alien reaches either horizontal edge."""
        return (
            self.rect.right >= self.boundaries.right
            or self.rect.left <= self.boundaries.left
        )

    def draw_alien(self):
        """Draw the alien at its current position."""
        self.screen.blit(
            self.image,
            self.rect
        )
