from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, 'white', (self.position[0], self.position[1]), self.radius, 2)
	def update(self, dt):
		self.position[0] += self.velocity[0] * dt
		self.position[1] += self.velocity[1] * dt
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS: return
		new_direction = random.uniform(20, 50)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid_1_direction = self.velocity.rotate(-new_direction)
		asteroid_2_direction = self.velocity.rotate(new_direction)
		asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
		asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
		asteroid_1.velocity = asteroid_1_direction * 1.5
		asteroid_2.velocity = asteroid_2_direction * 1.5
