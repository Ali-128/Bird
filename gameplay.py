import pygame
import sys
import objects
def run(width,height):
	pygame.init()
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption("Flying Bird")
	back=pygame.image.load('pictures/sky.png')
	bird=objects.Bird(screen,100,100,0,0,0.4)
	cloud=objects.Cloud(screen)
	pipes=[]
	scores=0
	for i in range(3):
		pipes.append(objects.Pipe(screen,i*300+300,4))
	while True:
		screen.blit(back,(0,0))
		cloud.show()
		cloud.update()
		bird.show()
		bird.update()
		for i in pipes:
			i.show()
			if not bird.gameover:
				scores=i.update(scores)
				bird.is_col(i)
		objects.print_text(screen,str(scores),(700,100))
		if bird.gameover:
			objects.print_text(screen,'GAME OVER',(screen.get_width()//2-95,screen.get_height()//2-30))
		pygame.display.update()
def main(args):
	run(800,600)
if __name__=='__main__':
	main(sys.argv)
