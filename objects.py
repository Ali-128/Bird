import pygame
class Bird:
	def __init__(self,screen,x,y,speed_x,speed_y,g):
		self.screen=screen
		self.x=x
		self.y=y
		self.speed_x=speed_x
		self.speed_y=speed_y
		self.g=g
		self.images=[pygame.image.load("pictures/redbird-downflap.png"),pygame.image.load("pictures/redbird-midflap.png"),pygame.image.load("pictures/redbird-upflap.png")]
		self.counter=0
	def gameover(self):
			text="Game Over"
			text_font=pygame.font.SysFont('freesansbold.ttf',50)
			textSurface=text_font.render(text,True,(255,255,255))
			textRect=textSurface.get_rect()
			textRect=((self.screen.get_width()//2-85),(self.screen.get_height()//2-30))
			self.screen.blit(textSurface,textRect)
			pygame.display.update()
	def update(self):
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
						self.speed_y-=self.g*40
		if self.speed_y > 0:
			self.speed_y+=self.g
		else:
			self.speed_y+=1.7*self.g
		self.y+=self.speed_y
		if self.y < 0 or self.y > self.screen.get_height():
			self.gameover()
			self.speed_y=0
			self.g=0
		self.counter+=1
		if self.counter == 3:
			self.counter = 0
	def show(self):
		self.screen.blit(self.images[self.counter % 3],(self.x,self.y))
class Pipe:
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
