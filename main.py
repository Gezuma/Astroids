# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this is where constants "variables" are assigned. Constants like SCREENWIDTH, ASTRIOD_MIN_RADIOS and ASTROID_SPAWN_RATE etc.
import constants

import player

def main():
    # initializing all pygame modules that can be initialized without arguments etc.
    pygame.init()
    clock_speed = pygame.time.Clock()  # object created to later set FPS
    dt = 0
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    
    # sets the display size for the game
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    player_obj = player.Player(x,y)


    # Game loop
    while True:
        # this should be at the beginning of the game loop, so the game can be closed by pressing the close button "X" on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # will be added later: 
        #  more checks for player inputs
        #  update the game world
        # will be added later: 
        #  more checks for player inputs
        #  update the game world

        player_obj.update(dt)
  
        screen.fill("black")  # display.flip() should always be at the end to refresh the screen
        player_obj.draw(screen) # refresh player object
        pygame.display.flip() # flips the pointers of back buffer we draw in - to the front buffer shown

        # limits framerate to 60 fps and set dt to amount of time since last it was called in seconds
        dt = clock_speed.tick(60)/1000 

        # limits framerate to 60 fps and set dt to amount of time since last it was called in seconds
        dt = clock_speed.tick(60)/1000 

if __name__ == "__main__":
    main()