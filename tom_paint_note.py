import pygame
import math
import time
import random
import csv
import datetime


pygame.init()
clock = pygame.time.Clock()

my_small_font = pygame.font.SysFont("Comic Sans MS", 50)
my_medium_font = pygame.font.SysFont("Comic Sans MS", 70)


BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED= (255,0,0)
YELLOW = (255, 255, 0)
BACKGROUND = WHITE

NEUTRAL = BLACK

if BACKGROUND == BLACK:
	NEUTRAL = WHITE
elif  BACKGROUND == WHITE:
	NEUTRAL = BLACK
else:
	NEUTRAL #= WHITE
	

screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
width,height = screen.get_size()

screen_width = width
screen_height = height

color_pallet_size = 80
paint_color = BLACK
pen_position = []
distance_with_erasor_global = [-1]

screen.fill(BACKGROUND)

#-----------------------------------------------
SMALL = 10
MIDDIUM = 20
BIG = 40
pen_size = SMALL
erasor_size = pen_size * 2

erase_mode = False
paint_mode = True
clear = False

# grow snake


	
def paint_2(x,y):
	  # PAINT MODE
	  
	   if erase_mode == True and paint_mode == False and y <= screen_height - 240 and y >= ot +  color_pallet_size:
	   	color = pygame.Rect(x , y ,  pen_size * 2, pen_size * 2)
	   	pygame.draw.rect(screen, paint_color, color)
	   if paint_mode == True and erase_mode == False and y <= screen_height - 230 and y >= ot +  color_pallet_size:
	   	color = pygame.Rect(x , y ,  pen_size, pen_size )
	   	pygame.draw.rect(screen, paint_color, color)
	  	


def paint(x,y):
	  # PAINT MODE
	  if  y <= screen_height - 230 and y >= ot +  color_pallet_size:
		   if erase_mode == True:
		   	color = pygame.Rect(x , y ,  pen_size * 2, pen_size * 2)
		   	pygame.draw.rect(screen, paint_color, color)
		   if paint_mode == True:
		   	color = pygame.Rect(x , y ,  pen_size, pen_size )
		   	pygame.draw.rect(screen, paint_color, color)
	  	
	  # ERASE MODE
	  
	 

def erasor(x,y):
	 color = pygame.Rect(x , y ,  erasor_size, erasor_size )
	 pygame.draw.rect(screen, BACKGROUND, color)



ot = 10 # offset from top
ob = 10 # offset from bottom
# color palett coordinates
red_coord = [ 0 , screen_height - 100  ]
green_coord = [ 110 , screen_height - 100  ]
yellow_coord = [ 220 , screen_height - 100  ]
white_coord = [ 330 , screen_height - 100  ]
blue_coord = [ 440 , screen_height - 100  ]


#size setting coordinates pallet

size_icon_small = [ 10 , screen_height - 210  ]
size_icon_middium = [ 110 , screen_height - 210  ]
size_icon_big = [ 220 , screen_height - 210]

#UPPER PALLET

paint_coord = [ color_pallet_size * 0 + 30 , ot  ]
shape_coord = [ color_pallet_size * 1 + 2 * 30 , ot ]
save_coord = [ color_pallet_size * 2 + 3 * 30, ot ]
erasor_coord = [ color_pallet_size * 3 + 4 * 30, ot ]
new_coord = [ color_pallet_size * 4 + 5 * 30, ot ]
what_color_coord = [ color_pallet_size *5 + 6 * 30, ot ]


# declare list variable to hold center info of color in color pallatte 
red_coord_center = [0,0]
green_coord_center = [0,0]
yellow_coord_center = [0,0]
white_coord_center = [0, 0]
blue_coord_center = [0, 0]
erasor_coord_center = [0, 0]

size_icon_small_rect_center = [0,0]
size_icon_middium_rect_center = [0,0]
size_icon_big_rect_center = [0,0]

paint_coord_center = [ 0, 0]
shapes_coord_center = [ 0,0 ]
save_coord_center = [ 0, 0 ]
erasor_coord_center = [ 0,0 ]
new_coord_center = [ 0, 0 ]
what_color_coord_center = [ 0,0 ]

#def color_pallate():
	
color_red = pygame.Rect(red_coord[0] , red_coord[1], color_pallet_size , color_pallet_size )
color_green= pygame.Rect(green_coord[0] , green_coord[1] ,  color_pallet_size , color_pallet_size)
color_yellow = pygame.Rect(yellow_coord[0] , yellow_coord[1] ,  color_pallet_size , color_pallet_size )
color_white = pygame.Rect(white_coord[0] , white_coord[1] ,  color_pallet_size , color_pallet_size)
	 
color_blue = pygame.Rect(blue_coord[0] , blue_coord[1] ,  color_pallet_size , color_pallet_size)
	 
color_erasor = pygame.Rect(erasor_coord[0] , erasor_coord[1] ,  color_pallet_size , color_pallet_size)


# upper PALLET

paint_icon = pygame.Rect(paint_coord[0], paint_coord[1], color_pallet_size, color_pallet_size)

shape_icon= pygame.Rect(shape_coord[0], shape_coord[1], color_pallet_size, color_pallet_size)

save_icon= pygame.Rect(save_coord[0], save_coord[1], color_pallet_size, color_pallet_size)

new_icon= pygame.Rect(new_coord[0], new_coord[1], color_pallet_size, color_pallet_size)

what_color_icon= pygame.Rect(what_color_coord[0], what_color_coord[1], color_pallet_size, color_pallet_size)
	 
	 # PAINT SIZE OBJECT
size_icon_small_rect = pygame.Rect( size_icon_small[0] , size_icon_small[1] , color_pallet_size  ,  color_pallet_size )
	 
size_icon_middium_rect= pygame.Rect( size_icon_middium[0] , size_icon_middium[1] , int(color_pallet_size ),  int(color_pallet_size))
size_icon_big_rect = pygame.Rect( size_icon_big[0] , size_icon_big[1] , int(color_pallet_size ),  int(color_pallet_size ))


tool_small_image = pygame.image.load("tom_paint_objects/tool_size_small.png")

tool_middium_image = pygame.image.load("tom_paint_objects/tool_size_middium.png")

tool_big_image = pygame.image.load("tom_paint_objects/tool_size_big.png")


#tool_middium_image_l= [pygame.image.transform(tool_middium_image,  (color_pallet_size, color_pallet_size))]

tool_middium_image_l = [pygame.transform.scale(tool_middium_image, (color_pallet_size, color_pallet_size))]

tool_small_image_l = [pygame.transform.scale(tool_small_image,  (color_pallet_size, color_pallet_size))]

tool_big_image_l= [pygame.transform.scale(tool_big_image,  (color_pallet_size, color_pallet_size))]

# LOWER PALLET
red_coord_center[0] =   color_red.centerx		   
red_coord_center[1] =  color_red.centery
	 
green_coord_center[0] = color_green.centerx
green_coord_center[1] =  color_green.centery
	 
yellow_coord_center[0] =   color_yellow.centerx
yellow_coord_center[1] =  color_yellow.centery
	 
white_coord_center[0] = color_white.centerx
white_coord_center[1] =  color_white.centery
	 
blue_coord_center[0] = color_blue.centerx
blue_coord_center[1] =  color_blue.centery
	 
erasor_coord_center[0] = color_erasor.centerx
erasor_coord_center[1] =  color_erasor.centery
	 
size_icon_small_rect_center[0] = size_icon_small_rect.centerx
	 
size_icon_small_rect_center[1] = size_icon_small_rect.centery
	 
size_icon_middium_rect_center[0] = size_icon_middium_rect.centerx
size_icon_middium_rect_center[1] = size_icon_middium_rect.centery
	 
size_icon_big_rect_center[0] = size_icon_big_rect.centerx
size_icon_big_rect_center[1] = size_icon_big_rect.centery
	 
# UPPER PALLET
paint_coord_center[0] =   color_red.centerx		   
paint_coord_center[1] =  color_red.centery
	 
shapes_coord_center[0] = shape_icon.centerx
shapes_coord_center[1] =  shape_icon.centery
	 
save_coord_center[0] =   save_icon.centerx
save_coord_center[1] =  save_icon.centery
	 
new_coord_center[0] = new_icon.centerx
new_coord_center[1] =  new_icon.centery
	 
what_color_coord_center[0] = what_color_icon.centerx
what_color_coord_center[1] =  what_color_icon.centery

#def color_pallate():	 
#BLIT LOWER PALLETE


pygame.draw.rect(screen, RED, color_red)
pygame.draw.rect(screen, GREEN, color_green)
pygame.draw.rect(screen,YELLOW , color_yellow)
pygame.draw.rect(screen, NEUTRAL , color_white)
pygame.draw.rect(screen, BLUE , color_blue)

# BLIT PAINT SIZE SETTING
#pygame.draw.rect(screen, GREEN, size_icon_small_rect)
screen.blit(tool_small_image_l[0], (size_icon_small[0] , size_icon_small[1]))

#pygame.draw.rect(screen, RED, size_icon_middium_rect)
screen.blit(tool_middium_image_l[0], (size_icon_middium[0] , size_icon_middium[1]))
#pygame.draw.rect(screen, RED, size_icon_big_rect)
screen.blit(tool_big_image_l[0], (size_icon_big[0] , size_icon_big[1]))
	 # BLIT upper PALLET
#pygame.draw.rect(screen, (100,100,100), color_erasor)
erasor_image = pygame.image.load("tom_paint_objects/erasor_0.png")

save_image = pygame.image.load("tom_paint_objects/save_0.png")

paint_image = pygame.image.load("tom_paint_objects/paint_0.png")

shape_image = pygame.image.load("tom_paint_objects/shapes_0.png")

new_image = pygame.image.load("tom_paint_objects/new_0.png")

save_image_l = [pygame.transform.scale(save_image, (color_pallet_size, color_pallet_size))]

paint_image_l = [pygame.transform.scale(paint_image, (color_pallet_size, color_pallet_size))]

shapes_image_l = [pygame.transform.scale(shape_image, (color_pallet_size, color_pallet_size))]

save_image_l = [pygame.transform.scale(save_image, (color_pallet_size, color_pallet_size))]

erasor_image_l = [pygame.transform.scale(erasor_image, (color_pallet_size, color_pallet_size))]

new_image_l = [pygame.transform.scale(new_image, (color_pallet_size, color_pallet_size))]







screen.blit( save_image_l[0], (save_coord[0] , save_coord[1]))

screen.blit( paint_image_l[0], (paint_coord[0] , paint_coord[1]))

screen.blit( shapes_image_l[0], (shape_coord[0] , shape_coord[1]))


screen.blit( erasor_image_l[0], (erasor_coord[0] , erasor_coord[1]))

screen.blit( new_image_l[0], (new_coord[0] , new_coord[1]))

def show_paint_color(color):
	pygame.draw.circle(screen, color, (what_color_coord[0] + color_pallet_size * 0.5, what_color_coord[1] + color_pallet_size * 0.5) , color_pallet_size * 0.5, 20)


# CLEAR SCREEN FOR NEW PAIN JOB
def clear():
	screen.fill(BACKGROUND)
	pygame.draw.rect(screen, RED, color_red)
	pygame.draw.rect(screen, GREEN, color_green)
	pygame.draw.rect(screen,YELLOW , color_yellow)
	pygame.draw.rect(screen, NEUTRAL , color_white)
	pygame.draw.rect(screen, BLUE , color_blue)
	
	screen.blit( save_image_l[0], (save_coord[0] , save_coord[1]))

	screen.blit( paint_image_l[0], (paint_coord[0] , paint_coord[1]))

	screen.blit( shapes_image_l[0], (shape_coord[0] , shape_coord[1]))

	screen.blit( erasor_image_l[0], (erasor_coord[0] , erasor_coord[1]))

	screen.blit( new_image_l[0], (new_coord[0] , new_coord[1]))
	
	screen.blit(tool_small_image_l[0], (size_icon_small[0] , size_icon_small[1]))

#pygame.draw.rect(screen, RED, size_icon_middium_rect)
	screen.blit(tool_middium_image_l[0], (size_icon_middium[0] , size_icon_middium[1]))
#pygame.draw.rect(screen, RED, size_icon_big_rect)
	screen.blit(tool_big_image_l[0], (size_icon_big[0] , size_icon_big[1]))


# SAVE FILE NAME NAME NAME NAME	 
file_name_l = []


def save_screen():
	
	save_time = pygame.time.get_tick()
	
	if current_time - save_time < = 2000:
		
		
		pygame.draw.rect(screen,BACKGROUND,pygame.Rect(0,0, screen_width,color_pallet_size + 20))
		
		pygame.draw.rect(screen,BACKGROUND,pygame.Rect(0, screen_height -  color_pallet_size * 2.7 , screen_width, color_pallet_size * 2.5))
		
	
	
	file_name = "thomas_kitaba"
	t = time.localtime()
 

	date_object = datetime.date.today()
	current_time = time.strftime("%H-%M-%S", t)
	file_name = file_name + str(date_object) +str(current_time) + ".jpeg"

	enter_name = my_medium_font.render(" Saved with  FILE NAME", 1, NEUTRAL)
	#pygame.draw.rect(screen,(255,255,0),pygame.Rect(80,140,550,80), 2)
	
	screen.blit(enter_name,(100, 10 ))
					
	file_name_txt= my_small_font.render(str(file_name), 1,(255,0, 0))		
	screen.blit(file_name_txt, (50, color_pallet_size * 0.5 + 25))
	#return file_name
	pygame.image.save(screen, file_name)
	
	pygame.display.update()
	
				 	 			 	 
	
#	if detail == 1: display small list
#if detail == 2 display large list
				#################
				#######GAME######
				#######START######
				#################
		
running = True
while running:
	#clock.tick(2000)
	current_time = pygame.time.get_ticks()
	
	#screen.fill((0,0,0))
	current_time = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
			
			# change mousedown to mousedrage
			
		if event.type == pygame. MOUSEBUTTONDOWN:
			#check which button is clicked
			mousex, mousey = pygame.mouse.get_pos()
		
				# distance with red
			distance_with_red = int(math.sqrt((red_coord_center[0] - mousex)**2 + (red_coord_center[1] - mousey)**2))
			
			# distance with green
			distance_with_green = int(math.sqrt((green_coord_center[0] - mousex)**2 + (green_coord_center[1] - mousey)**2))
			
			# distance with yellow
			distance_with_yellow = int(math.sqrt((yellow_coord_center[0] - mousex)**2 + (yellow_coord_center[1] - mousey)**2))
			
			# distance with neutral
			distance_with_neutral = int(math.sqrt((white_coord_center[0] - mousex)**2 + (white_coord_center[1] - mousey)**2))
			
			# distance with blue
			distance_with_blue = int(math.sqrt((blue_coord_center[0] - mousex)**2 + (blue_coord_center[1] - mousey)**2))
			
			# distance with ERASOR
			distance_with_erasor = int(math.sqrt((erasor_coord_center[0] - mousex)**2 + (erasor_coord_center[1] - mousey)**2))
			
			distance_with_size_small = int(math.sqrt((size_icon_small_rect_center[0] - mousex)**2 + (size_icon_small_rect_center[1] - mousey)**2))
			distance_with_size_middium = int(math.sqrt((size_icon_middium_rect_center[0] - mousex)**2 + (size_icon_middium_rect_center[1] - mousey)**2))
			distance_with_size_big = int(math.sqrt((size_icon_big_rect_center[0] - mousex)**2 + (size_icon_big_rect_center[1] - mousey)**2))
			
# DISTANCE WITH UPPER ICONS

# save_coord_center[1] =  color_yellow.centery
#new_coord_center[0] = color_white.centerx
#what_color_coord_center[0] = color_blue.cente

			distance_with_save = int(math.sqrt((save_coord_center[0] - mousex)**2 + (save_coord_center[1] - mousey)**2))
			
			distance_with_new = int(math.sqrt((new_coord_center[0] - mousex)**2 + (new_coord_center[1] - mousey)**2))
			
			distance_with_what_color = int(math.sqrt((what_color_coord_center[0] - mousex)**2 + (what_color_coord_center[1] - mousey)**2))
			
			
			
			
			if distance_with_green <= color_pallet_size * 0.5:
				erase_mode = False
				paint_mode = True		
			
				paint_color = GREEN
				
				
			if distance_with_red <= color_pallet_size * 0.5:
				erase_mode = False
				paint_mode = True	
				paint_color = RED
				
			if distance_with_yellow <= color_pallet_size * 0.5:
				erase_mode = False
				paint_mode = True	
				paint_color = YELLOW
				
			if distance_with_neutral <= color_pallet_size * 0.5:
				erase_mode = False
				paint_mode = True	
				paint_color = NEUTRAL
			
			if distance_with_blue <= color_pallet_size * 0.5:
				paint_color = BLUE
				#pygame.image.save(screen, "screenshot.jpeg")
			
			if distance_with_erasor <= color_pallet_size * 0.5 + 10:
				
				distance_with_erasor_global[0] = distance_with_erasor
				erase_mode = True
				paint_mode = False	
				paint_color = BACKGROUND
				#clear()
				#erase(mousex, mousey)
				
			if distance_with_size_small <= color_pallet_size :
				pen_size = SMALL
				
			if distance_with_size_middium <= color_pallet_size:
				pen_size = MIDDIUM
			if distance_with_size_big <= color_pallet_size:
				pen_size = BIG
				
			# UPPER PALLET ICON CLICKED
			# save jpeg format
			if distance_with_save <= color_pallet_size:
					 save_screen()
					
					#pygame.image.save(screen, "tomas_kitaba_paint.jpeg")
			
			if distance_with_new <= color_pallet_size:
				#clear = True
				clear()
				
			if distance_with_what_color <= color_pallet_size:
				
				if BACKGROUND == BLACK: 
					BACKGROUND =WHITE
				if BACKGROUND == WHITE:
				 	BACKGROUND = BLACK
			#
				
					
					
				
				
				
	
		if pygame.mouse.get_pressed()[0]:
			mousex, mousey = pygame.mouse.get_pos()
			
			pen_position.append([mousex,mousey])
			show_paint_color(paint_color)
			#for i  in pen_position:
				#paint(i[0],i[1])
			paint(mousex,mousey)
			
			
			
			
			
			
			
		#color_pallate()
	
	pygame.display.update()
				
	
				
	
	
