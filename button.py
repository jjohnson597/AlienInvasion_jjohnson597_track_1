"""
Program: Alien Invasion: Side Strike - Track 1
Author: Jaylen Johnson
Purpose: Creates and manages the clickable Play button displayed when
the game is inactive.
Starter Code: Adapted from the Alien Invasion starter project:
https://github.com/jjohnson597/alien_Invasion_starter3
Date: 07/26/2026
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """Create and manage a clickable game button."""

    def __init__(
        self,
        game: "AlienInvasion",
        msg: str
    ):
        """Initialize the button and prepare its displayed message."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.button_font_size
        )

        self.rect = pygame.Rect(
            0,
            0,
            self.settings.button_width,
            self.settings.button_height
        )

        self.rect.center = self.boundaries.center

        self._prep_msg(msg)

    def _prep_msg(self, msg: str):
        """Render the button message and center it within the button."""
        self.msg_image = self.font.render(
            msg,
            True,
            self.settings.text_color,
            None
        )

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button and its centered message on the screen."""
        self.screen.fill(
            self.settings.button_color,
            self.rect
        )

        self.screen.blit(
            self.msg_image,
            self.msg_image_rect
        )

    def check_clicked(self, mouse_pos) -> bool:
        """Return True when the supplied mouse position is over the button."""
        return self.rect.collidepoint(mouse_pos)