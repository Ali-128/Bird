import pygame
import sys
import objects
def run(width,height):
	pygame.init()
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption("Flying Bird")
	back=pygame.image.load('pictures/sky.png')
	bird=objects.Bird(screen,100,100,0,0,0.1)
	pipes=[]
	for i in range(4):
		pipes.append(objects.Pipe(screen))
	while True:
		screen.blit(back,(0,0))
		bird.show()
		bird.update()
		for i in pipes:
			bird.is_col(i)
		pygame.display.update()
def main(args):
	run(800,600)
if __name__=='__main__':
	main(sys.argv)
