import pygame
class Bird:
	def __init__(self,screen,bird_x,bird_y,speed_X,speed_Y):
		self.screen=screen
		self.bird_x=bird_x
		self.bird_y=bird_y
		self.speed_X=speed_X
		self.speed_Y=speed_Y
		self.image=pygame.image.load("pictures/redbird-upflap.png")
		
	def update(self):
		pass
	def show(self):
		pass
class Stuff:
	def __init__(self,screen):
		self.screen=screen
		pass
	def update(self):
		pass
	def show(self):
		pass
class Cloud:
	def __init__(self,screen):
		self.screen=screen
		pass
	def update(self):
		pass
	def show(self):
		pass
