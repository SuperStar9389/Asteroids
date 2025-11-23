from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import *
import pygame

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0
		self.powerup_timer = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		color = "white"
		if self.powerup_timer > 0: color = "purple"
		pygame.draw.polygon(screen, color, self.triangle())

	def update(self, dt):
		keys = pygame.key.get_pressed()
		canshoot = self.shoot_timer <= 0
		if self.powerup_timer > 0:
			canshoot = True
			self.powerup_timer -= dt
		if canshoot: 
			self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		else: 
			self.shoot_timer -= dt
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_SPACE] and canshoot:
			self.shoot()
		

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.powerup_timer > 0: 
			for angle in [-45, -30,-15, 0, 15, 30, 45]:
				shot = Shot(self.position[0], self.position[1])
				shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + angle) * PLAYER_SHOOT_SPEED
			return
		shot = Shot(self.position[0], self.position[1])
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
		
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt