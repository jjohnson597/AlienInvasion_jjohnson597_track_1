import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()
    
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.game.settings
        self.boundaries = fleet.game.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien horizontally."""
        self.x += (
            self.settings.alien_speed
            * self.fleet.alien_direction
        )
        self.rect.x = self.x
        # removed undefined `temp_speed` usage; horizontal movement already applied above

    def check_edges(self):
        """Return True if the alien is at either screen edge."""
        return (
        self.rect.right >= self.boundaries.right
        or self.rect.left <= self.boundaries.left
    )

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
        
