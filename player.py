import circleshape
import pygame #  technically also avaible from former import with a circleshape. infront, but I think that makes it harder to read
import constants

class Player(circleshape.CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, constants.PLAYER_RADIUS)
    self.rotation = 0

  # in the player class
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen):
    width = 2
    color = "white"
    pygame.draw.polygon(screen, color, self.triangle(), width)