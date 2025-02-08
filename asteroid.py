from circleshape import *
import random
from constants import *


class Asteroid(CircleShape):

    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        
        Rotation1 = self.velocity.rotate(angle)
        Rotation2 = self.velocity.rotate(-angle)
        
        NewRadius = self.radius - ASTEROID_MIN_RADIUS
        
        X = Asteroid(self.position.x, self.position.y, self.radius - NewRadius)
        X.velocity += Rotation1*2
        Y = Asteroid(self.position.x, self.position.y, self.radius - NewRadius)
        Y.velocity += Rotation2*2