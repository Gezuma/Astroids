# Standard library imports
from abc import ABC, abstractmethod

# Third-party imports
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, radius):
        # We will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    def collision_detect(self, other_circle):
        return self.position.distance_to(other_circle.position) <= (self.radius + other_circle.radius)
