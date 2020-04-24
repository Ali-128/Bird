import pygame
class Bird:
	def __init__(self,screen,bird_x,bird_y,speed_X,speed_Y):
		self.screen=screen
		self.bird_x=bird_x
		self.bird_y=bird_y
		self.speed_X=speed_X
		self.speed_Y=speed_Y
		self.image=pygame.image.load("pictures/redbird-midflap.png")
	gameExit=False
	def update(self):
		while not gameExit:
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_UP:
						self.bird_y+=0.5
				elif event.type==pygame.KEYUP:
					if event.key==pygame.K_UP:
						self.bird_y+=0
				else:
					gameExit=True
					gameover()
	
	def show(self):
		self.screen.blit("pictures/redbird-midflap.png",(self.bird_x,self.bird_y))
		while not gameExit:
			for event in pygame.event.get():
				if event.type==pygame.KEYUP:
					if event.key==pygame.K_UP:
						self.screen.blit("pictures/redbird-upflap.png",(self.bird_x,self.bird_y))
				else:
					self.screen.blit('pictures/redbird-downflap.png',(self.bird_x,self.bird_y))
				pygame.display.update()
					
	def gameover(self):
			text="Game Over"
			text_font=pygame.font.SysFont('freesansbold.ttf',50)
			textSurface=text_font.render(text,True,(255,255,255))
			textRect=textSurface.get_rect()
			textRect=((self.screen.get_width()//2),(self.screen.get_height()//2))
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
