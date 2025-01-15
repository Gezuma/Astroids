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

def main():
    # Initializing all pygame modules that can be initialized without arguments etc.
    pygame.init()
    clock_speed = pygame.time.Clock()  # object created to later set FPS
    dt = 0
    
    # Sets the display size for the game
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # Set up groups and containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfields = pygame.sprite.Group()
    
    player.Player.containers = (updatable, drawable) 
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
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
            if player_obj.collision_detect(asteroid_obj):
                print("Game over!")
                sys.exit()

        # Render frame
        screen.fill("black")  # background    
        for draws in drawable:
            draws.draw(screen) # each obj instance added to the drawable group is drawn 
        
        pygame.display.flip() # flips the pointers of back buffer we draw in - to the front buffer shown

        dt = clock_speed.tick(constants.FRAMES_PER_SECOND)/1000  # sets framerate 

if __name__ == "__main__":
    main()