# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
       for event in pygame.event.get(): # Check for player trying to use X button to close the game and quits game if pressed
            if event.type == pygame.QUIT:
                return
       pygame.Surface.fill(screen, (0, 0, 0)) # Make a black screen for the game
       pygame.display.flip()    # Refresh game screen








if __name__ == "__main__":
 main()