import pygame
import sys

def run(width,height):
	pygame.init()
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption("Flying Bird")
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit(0)
def main(args):
	run(500,500)
if __name__=='__main__':
	main(sys.argv)
