# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *




def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while True:
       for event in pygame.event.get(): # Check for player trying to use X button to close the game and quits game if pressed
            if event.type == pygame.QUIT:
                return
       pygame.Surface.fill(screen, (0, 0, 0)) # Make a black screen for the game
       player.draw(screen) # Render our player on screen
       pygame.display.flip()    # Refresh game screen
       

       dt = (clock.tick(60) / 1000) # Set refresh rate to 60 and save DeltaTime in dt variable








if __name__ == "__main__":
 main()