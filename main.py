# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

updateables = pygame.sprite.Group()
drawables = pygame.sprite.Group()

asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updateables, drawables)
Asteroid.containers = (updateables, drawables, asteroids)
AsteroidField.containers = (updateables)
Shot.containers = (updateables,drawables, shots)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    AF = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(150,150,150))

        ## Update
        for sprite in updateables:
            sprite.update(dt)
        ## Draw
        for sprite in drawables:
            sprite.draw(screen)
        ## Collision
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        # player.update(dt)
        # player.draw(screen)
        
        pygame.display.flip()
        
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()