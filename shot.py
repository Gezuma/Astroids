# Third-party imports
import pygame

# Local imports
import circleshape
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, position, radius):
        super().__init__(position[0], position[1], radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, constants.SHOT_RADIUS) 
    
    def update(self, dt):
        self.position += self.velocity * constants.PLAYER_SHOOT_SPEED * dt 
