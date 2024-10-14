# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import *
from player import Player
from asteroid import Asteroid
from constants import *




def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Create groups to clean up our game loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    # Add player to both groups
    updatable.add(player)
    drawable.add(player)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get(): # Check for player trying to use X button to close the game and quits game if pressed
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0)) # Make a black screen for the game
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()    # Refresh game screen
            
        
        dt = (clock.tick(60) / 1000) # Set refresh rate to 60 and save DeltaTime in dt variable








if __name__ == "__main__":
 main()