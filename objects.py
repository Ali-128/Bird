import pygame
class Bird:
	def __init__(self,screen,bird_x,bird_y,speed_X,speed_Y):
		self.screen=screen
		self.bird_x=bird_x
		self.bird_y=bird_y
		self.speed_X=speed_X
		self.speed_Y=speed_Y
<<<<<<< HEAD
		self.image=pygame.image.load("picture/redbird-midflap.png")
=======
		self.image=pygame.image.load("pictures/redbird-upflap.png")
>>>>>>> b973c73899ec82834b120dfdbc792b81f9642b7d
		
	def update(self):
		pass
	def show(self):
		pass
	def gameover(self):
		text="Game Over"
		text_font=pygame.font.Font('freesansbold',50)
		textSurface=text_font.render(text,True,(255,255,255))
		textRect=textSurface.get_rect()
		textRect=((self.screen.get_width()//2),self.screen.get_height//2)
		self.screen.blit(textSurface,textRect)
		pygame.display.update()
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
