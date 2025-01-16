# Standard library imports
import sys

# Third-party imports
import pygame

# Local imports
import constants # Game configuration constants
import player
import asteroid
import asteroidfield
import circleshape
import shot

def main():
    # Initializing all pygame modules that can be initialized without arguments etc.
    pygame.init()
    clock_speed = pygame.time.Clock()  # object created to later set FPS
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))   # Sets the display size for the game

    # Set up groups and containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfields = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    player.Player.containers =      (updatable, drawable)
    shot.Shot.containers =          (updatable, drawable, shots) 
    asteroid.Asteroid.containers =  (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = updatable

    # Initialize game objects
    player_obj = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield_obj = asteroidfield.AsteroidField()

    # Game loop
    while True:
        # Close the game by pressing the close button "X" in top right corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update game state
        for updates in updatable:
            updates.update(dt) # each obj instance added to the updatable group is updated 

        # Check collisions
        for asteroid_obj in asteroids:
            if asteroid_obj.collision_detect(player_obj):
                print("Game over!")
                sys.exit()
            for shot_obj in shots:
                if shot_obj.collision_detect(asteroid_obj):
                    shot_obj.kill()
                    asteroid_obj.split()


        # Render frame
        screen.fill("black")  # background    
        for draws in drawable:
            draws.draw(screen) # each obj instance added to the drawable group is drawn 
        
        pygame.display.flip() # flips the pointers of back buffer we draw in - to the front buffer shown

        dt = clock_speed.tick(constants.FRAMES_PER_SECOND)/1000  # sets framerate 

if __name__ == "__main__":
    main()