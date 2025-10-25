from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)
	def draw(self, screen):
		pygame.draw.circle(screen, 'blue', (self.position[0], self.position[1]), self.radius, 2)
	def update(self, dt):
		self.position[0] += self.velocity[0] * dt
		self.position[1] += self.velocity[1] * dt