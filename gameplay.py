import pygame
import sys
import objects
def run(width,height):
	pygame.init()
	screen=pygame.display.set_mode((width,height))
<<<<<<< HEAD
	pygame.display.set_caption("Flying Bird")
=======
	bird=objects.Bird(screen)
	stuffs=[]
>>>>>>> 34d8c138efd0a0f47a80715728d648dd6b306d72
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit(0)
		screen.fill((255,255,255))
		bird.update()
		bird.show()
		pygame.display.update()
def main(args):
	run(500,500)
if __name__=='__main__':
	main(sys.argv)
