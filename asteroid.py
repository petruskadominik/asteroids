import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width = 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20, 50)
            print(random_angle)
            asteroid_1 = self.velocity.rotate(random_angle)
            asteroid_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_1.velocity = asteroid_1
            split_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_2.velocity = asteroid_2
            self.kill()


