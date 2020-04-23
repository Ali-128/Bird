import pygame
class Bird:
	def __init__(self,screen,x_bird,y_bird,speed_X,speed_Y):
		self.screen=screen
		self.x_bird=x_bird
		self.y_bird=y_bird
		self.speed_X=speed_X
		self.speed_Y=speed_Y
		self.image=pygame.image.load("redbird-upflap.png")
		
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
