import pygame
import math
import time
import random
import csv


pygame.init()
clock = pygame.time.Clock()


BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)
BACKGROUND = WHITE

screen = pygame.display.set_mode((600,600))


#========= SNAKE BODY AND FOOD ======
# grow snake


def draw_food(x,y):
	food_rectangle = pygame.Rect(x,y,block,block)
	food_rectangle_coord = [food_rectangle.centerx, food_rectangle.centery]
	
	screen.blit(snake_image, (x,y))
	pygame.draw.rect(screen, BLUE, food_rectangle )
				#################
				#######GAME######
				#######START######
				#################
running = True
while running:
	clock.tick(20)
	current_time = pygame.time.get_ticks()
	
	#screen.fill((0,0,0))
	screen.fill(BACKGROUND)
	
	current_time = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
			
			
		if event.type == pygame. MOUSEBUTTONDOWN:
			pass
			
	
	pygame.display.update()
				
	
				
	
	
