import pygame
pictures={'mid_bird':'pictures/redbird-midflap.png',
          'up_bird':'pictures/redbird-upflap.png',
          'down_bird':'pictures/redbird-downflap.png',
          'green_pipe':'pictures/pipe-green.png',
          'red_pipe_up':'pictures/red-pipe.png',
          'red_pipe_down':'pictures/red-pipe-d.png',
          'cloud':'pictures/cloud.png',
          'base':'pictures/base.png',
          'sky':'pictures/sky.png',
          'white_cloud':'pictures/w-cloud.png'
          }
class Bird:
	def __init__(self,screen,bird_x,bird_y,speed_x,speed_y,y_change):
		self.screen=screen
		self.bird_x=bird_x
		self.bird_y=bird_y
		self.speed_x=speed_x
		self.speed_y=speed_y
		self.y_change=y_change
		self.images=[pygame.image.load("pictures/redbird-downflap.png"),pygame.image.load("pictures/redbird-midflap.png"),pygame.image.load("pictures/redbird-upflap.png")]
		self.counter=0
	def gameover(self):
			text="Game Over"
			text_font=pygame.font.SysFont('freesansbold.ttf',50)
			textSurface=text_font.render(text,True,(255,0,0))
			textRect=textSurface.get_rect()
			textRect=((self.screen.get_width()//2-95),(self.screen.get_height()//2-30))
			self.screen.blit(textSurface,textRect)
			pygame.display.update()
	def update(self):
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
						self.speed_y-=self.y_change*40
		if self.speed_y > 0:
			self.speed_y+=self.y_change
		else:
			self.speed_y+=1.7*self.y_change
		self.bird_y+=self.speed_y
		if self.bird_y < 0 or self.bird_y > self.screen.get_height():
			self.gameover()
			self.speed_y=0
			self.y_change=0
		self.counter+=1
		if self.counter == 3:
			self.counter = 0
	def show(self):
<<<<<<< HEAD
		self.screen.blit(self.images[self.counter % 3],(self.bird_x,self.bird_y))
class Stuff:
=======
		self.screen.blit(self.images[self.counter % 3],(self.x,self.y))
class Pipe:
>>>>>>> 4813647cae89b1d4c17dc94d987912783d4ba3a7
	def __init__(self,screen):
		self.screen=screen
		self.xpos=self.screen.get_width()
		self.ypos_u=random()*self.screen.get_height()
		self.ypos_d=random()*self.screen.get_height()
		self.uppipe=pygame.image.laod('pipe-green.png')
		self.downpipe=pygame.image.load('pip-green-d.png')
	def update(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pass
		self.xpos+=-3
	def show(self):
		self.screen.blit(self.uppipe, (self.xpos, self.ypos_u))
		self.screen.blit(self.downpipe, (self.xpos, self.ypos_d))
class Cloud:
	def __init__(self,screen):
		self.screen=screen
		self.cloud=pygame.image.load('w-cloud-new.png')
		self.xpos=self.screen.get_width()
		self.ypos=random()*self.screen.get_height()
	def update(self):
		self.xpos+=-5
	def show(self):
		self.screen.blit(self.cloud, (self.xpos, self.ypos))
