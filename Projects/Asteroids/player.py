# player.py
import pygame
# Import the CircleShape class (assuming it's defined in another file)
from circleshape import *  # Adjust the import if CircleShape is in the same file
from shot import Shot
# Import the PLAYER_RADIUS constant from constants.py
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # Initialize the rotation field to 0
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        
        # Get the list of points for the triangle
        points = self.triangle()
        
        # Draw the triangle using pygame.draw.polygon
        pygame.draw.polygon(screen, "white", points, 2)
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
