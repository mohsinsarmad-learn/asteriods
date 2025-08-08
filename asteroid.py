import pygame, random
from circleshape import CircleShape
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
)


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 30)

        v1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        v2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)

        new_radious = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position.x, self.position.y, new_radious)
        new_asteroid.velocity = v1 * 1.2

        new_asteroid = Asteroid(self.position.x, self.position.y, new_radious)
        new_asteroid.velocity = v2 * 1.2
