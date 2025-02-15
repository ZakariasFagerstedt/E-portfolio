import pygame
import sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    score = 0
    font = pygame.font.Font(None, 36)  # None: Default font, 36: Font size
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                screen.fill((255, 0, 0))
                pygame.display.flip()
                pygame.time.wait(100)  # pause for 100ms to show the flash
                print("Game over!")
                print(score)
                pygame.quit()
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
                    score += 100

        pygame.Surface.fill(screen,(0,0,0))

        text_surface = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(text_surface, (10, 10))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
