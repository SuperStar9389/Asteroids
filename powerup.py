from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame

class PowerUp(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, ASTEROID_MIN_RADIUS * 2)
	def draw(self, screen):
		pygame.draw.circle(screen, 'green', (self.position[0], self.position[1]), self.radius, 2)
	def update(self, dt):
		self.position[0] += self.velocity[0] * dt
		self.position[1] += self.velocity[1] * dt