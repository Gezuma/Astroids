# Standard Libraries imports
import random

# Third-party imports
import pygame

# Local imports
import circleshape
import constants

class Asteroid(circleshape.CircleShape):
    total_asteroids = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
      
      #  for future expansion:
      ###########################################################################
      #  Asteroid.total_asteroids += 1
      #  print(Asteroid.total_asteroids)
    
   
    #def kill(self):
    #    super().kill()
      #  Asteroid.total_asteroids -= 1 
      #  print(Asteroid.total_asteroids)

      #  Write text "Asteroids: Asteroid.total_asteroids" to screen  ... add highscore based on kills and how difficult, difficulty based on amount of Asteroids
      #  Add bonus lives, that are used when dieing, blinks the ship for a couple of seconds of immortality, and add more bonus lives at different highs of highscore
       
      #  Play explosion sound and add visual effect here
      ##########################################################################
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2) 
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        asteroid = self
        asteroid.kill()
        if asteroid.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        rnd_angle = random.uniform(15, 40) # assignment said between 20 and 50, but I prefer 15 and 40
        vect_1 = asteroid.velocity.rotate(rnd_angle)
        vect_2 = asteroid.velocity.rotate(-rnd_angle)

        new_radius = asteroid.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
        new_asteroid_2 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)

        # Scale up the velocity slightly to make the newly spawned asteroids faster
        new_asteroid_1.velocity = vect_1* 1.2
        new_asteroid_2.velocity = vect_2* 1.2