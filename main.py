from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    dt = 0
    while True:
        screen.fill("black")
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if player.iscolliding(asteroid): 
                print("Game over!")
                return
            for shot in shots:
                if shot.iscolliding(asteroid):
                    shot.kill()
                    asteroid.split()
            
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        print("FPS: ", str(1 / dt))


if __name__ == "__main__":
    main()
