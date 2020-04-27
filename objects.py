import pygame
import random
pictures={'mid_bird':'pictures/redbird-midflap.png',
          'up_bird':'pictures/redbird-upflap.png',
          'down_bird':'pictures/redbird-downflap.png',
          'green_pipe_u':'pictures/pipe-green-u.png',
		  'green_pipe_d':'pictures/pipe-green-d.png',
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
		self.gameover=False
		self.images=[pygame.image.load(pictures['down_bird']),pygame.image.load(pictures['mid_bird']),pygame.image.load(pictures['up_bird'])]
		self.counter=0
	def __gameover(self):
			self.speed_y=0
			self.y_change=0
			self.gameover=True
			text="Game Over"
			text_font=pygame.font.SysFont('freesansbold.ttf',50)
			textSurface=text_font.render(text,True,(255,0,0))
			textRect=((self.screen.get_width()//2-95),(self.screen.get_height()//2-30))
			self.screen.blit(textSurface,textRect)
			pygame.display.update()
	def update(self):
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE and not self.gameover:
						self.speed_y-=self.y_change*40
		if self.speed_y > 0:
			self.speed_y+=1.1*self.y_change
		else:
			self.speed_y+=3*self.y_change
		self.bird_y+=self.speed_y
		if self.bird_y < 0 or self.bird_y > self.screen.get_height():
			self.__gameover()
		self.counter+=1
		if self.counter == 3:
			self.counter = 0
	def show(self):
		self.screen.blit(self.images[self.counter],(self.bird_x,self.bird_y))
	def is_col(self,pipe):
		if self.bird_x>pipe.xpos and self.bird_x<pipe.xpos+pipe.downpipe.get_width()+self.images[self.counter].get_width():
			if self.bird_y<pipe.y2 or self.bird_y+self.images[self.counter].get_height()>pipe.y1:
				self.__gameover()
class Pipe:
	def __init__(self,screen,xpos,speed_x):
		self.screen=screen
		self.speed_x=speed_x
		self.width=screen.get_width()
		self.height=screen.get_height()
		self.uppipe=pygame.image.load(pictures['green_pipe_u'])
		self.downpipe=pygame.image.load(pictures['green_pipe_d'])
		self.__newpipe(xpos)
		pygame.display.update()
	def __newpipe(self,xpos):
		self.xpos=xpos
		self.ypos_u=(random.random()*self.height/4)+self.height/2 +12
		self.y1=self.ypos_u
		self.y2=random.random()*self.height/4 + self.height/4 -12
		self.ypos_d=self.y2 - self.downpipe.get_height()
	def update(self,scores):
		self.xpos-=self.speed_x
		if self.xpos+self.uppipe.get_width()<0:
			scores+=1
			self.__newpipe(self.width)
		return scores
	def show(self):
		self.screen.blit(self.uppipe, (self.xpos, self.ypos_u))
		self.screen.blit(self.downpipe, (self.xpos, self.ypos_d))
class Cloud:
	def __init__(self,screen):
		self.screen=screen
		self.cloud=pygame.image.load(pictures['white_cloud'])
		'''self.xpos=self.screen.get_width()
		self.ypos=random.random()*self.screen.get_height()'''
		self.__newcloud(self.screen.get_width())
	def __newcloud(self,xpos):
		self.xpos=xpos
		self.ypos=(self.screen.get_height()-self.cloud.get_height())*random.random()
	def update(self):
		self.xpos+=-5
	def show(self):
		self.screen.blit(self.cloud, (self.xpos, self.ypos))
