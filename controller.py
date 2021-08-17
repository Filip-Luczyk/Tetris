import pygame, view, time, random
from model import Manage

view.window_generator()

if __name__ == "__main__":
	y = 50
	while True:
		t0 = time.time()
		view.window_generator()
		Manage.Fall()
		positions = Manage.GetPositions()
		view.squares((100, 90, 200), positions, 50)
		pygame.display.flip()
		t1 = time.time()
		while t1 - t0 < 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit(0)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						Manage.MoveRight()
					elif event.key == pygame.K_LEFT:
						Manage.MoveLeft()
					elif event.key == pygame.K_UP:
						print('Nacisnąłeś UP')
					elif event.key == pygame.K_DOWN:
						print('Nacisnołeś DOWN')
					elif event.key == pygame.K_x:
						exit(0)
			positions = Manage.GetPositions()
			view.squares((100, 90, 200), positions, 50)
			pygame.display.flip()
			
			t1 = time.time()
