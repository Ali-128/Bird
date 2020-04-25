import pygame
import sys
import objects
def run(width,height):
	pygame.init()
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption("Flying Bird")
	back=pygame.image.load('pictures/sky.png')
	pipe=pygame.image.load('pictures/pipe-green.png')
	bird=objects.Bird(screen,100,100,0,0)
	while True:
		'''for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit(0)'''
		screen.blit(back,(0,0))
		screen.blit(pipe,(200,0))
		bird.update()
		bird.show()
		pygame.display.update()
def main(args):
	run(800,600)
if __name__=='__main__':
	main(sys.argv)
