from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame

def main():
    pygame.init()
    pygame.font.init()
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)
    PowerUp.containers = (powerups, drawable, updateable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score_font = pygame.font.Font(None, 36)
    score = 0
    field = AsteroidField()
    dt = -1
    while True:
        screen.fill("black")
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        fps_text = score_font.render(f"FPS: {int(1 / dt)}", True, (255, 255, 255))
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        screen.blit(score_text, (10, 10))
        screen.blit(fps_text, (10, 40))
        for asteroid in asteroids:
            if player.iscolliding(asteroid) and player.powerup_timer <= 0: 
                print("Game over!")
                return
        
            for shot in shots:
                if shot.iscolliding(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += SHOT_REWARD
        for powerup in powerups:
            if player.iscolliding(powerup):
                player.powerup_timer = PLAYER_POWERUP_DURATION
                print("Powerup!")
                powerup.kill()
            
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        print("FPS: ", str(1 / dt))


if __name__ == "__main__":
    main()
