
import random

import pygame

from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            randomDir = random.uniform(20, 50)
            firstAsteroidVelocity = self.velocity.rotate(randomDir)
            secondAsteroidVelocity = self.velocity.rotate(-randomDir)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            asterodi2 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid1.velocity = firstAsteroidVelocity * 1.2
            asterodi2.velocity = secondAsteroidVelocity * 1.2
