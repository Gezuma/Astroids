# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this is where constants "variables" are assigned. Constants like SCREENWIDTH, ASTRIOD_MIN_RADIOS and ASTROID_SPAWN_RATE etc.
import constants

def main():
    # initializing all pygame modules that can be initialized without arguments etc.
    pygame.init()
    print("Starting asteroids!")
    
    # sets the display size for the game
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print("Screen width: 1280")
    print("Screen height: 720")

    # Game loop
    while True:
        # this should be at the beginning of the game loop, so the game can be closed by pressing the close button "X" on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # stuff loop that need to loop

        # display.flip() should always be at the end to refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()