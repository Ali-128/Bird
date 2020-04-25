import pygame
class Bird:
	def __init__(self,screen,bird_x,bird_y,speed_X,speed_Y):
		self.screen=screen
		self.bird_x=bird_x
		self.bird_y=bird_y
		self.speed_X=speed_X
		self.speed_Y=speed_Y
		self.g=0.1
		self.go=False
		self.image=pygame.image.load("pictures/redbird-midflap.png")
	def gameover(self):
			text="Game Over"
			text_font=pygame.font.SysFont('freesansbold.ttf',50)
			textSurface=text_font.render(text,True,(255,255,255))
			textRect=textSurface.get_rect()
			textRect=((self.screen.get_width()//2),(self.screen.get_height()//2))
			self.screen.blit(textSurface,textRect)
			pygame.display.update()
	def update(self):
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
						self.speed_Y-=self.g*40
		if self.speed_Y > 0:
			self.speed_Y+=self.g
		else:
			self.speed_Y+=1.5*self.g
		self.bird_y+=self.speed_Y
		if self.bird_y < 0 or self.bird_y > self.screen.get_height():
			self.gameover()
			self.speed_Y=0
			self.g=0
	def show(self):
		self.screen.blit(self.image,(self.bird_x,self.bird_y))


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
