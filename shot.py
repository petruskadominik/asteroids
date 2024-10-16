import pygame
from circleshape import *
from constants import *

# Giving player ability to shoot at the asteroids as god intended

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt