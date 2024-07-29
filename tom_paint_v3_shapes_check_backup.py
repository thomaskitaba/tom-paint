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
BACKGROUND = BLACK

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

paint_coordinate = []
shape_coordinate  = [0,0,0,0]

paint_coordinate_line_cont = []
shape_coordinate_line_cont = [0,0,0,0]



screen.fill(BACKGROUND)

#-----------------------------------------------

erase_mode = False
paint_mode = True
shape_mode_line = False
shape_mode_rectangle= False
shape_mode_circle = False

clear = False

SMALL = 2
MIDDIUM = 6
BIG = 10

pen_size = SMALL
erasor_size = pen_size * 2


current_time = [0]
save_time = [0]
save_mode = False
save_mode = [0]

cleared = False # when NEW is clicked cleared is TRUE


# TOM_PAINT AUDIOS

save_sound = pygame.mixer.Sound("tom_paint_audios/save_sound_0.wav")

paint_drop_sound = pygame.mixer.Sound("tom_paint_audios/paint_drop_1.mp3")

shapes_rolling = pygame.mixer.Sound("tom_paint_audios/shapes_rolling_0.mp3")

paper_rustle = pygame.mixer.Sound("tom_paint_audios/paper_rustle_0.mp3")
# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/crumbling-paper-87

pencil_sharpener = pygame.mixer.Sound("tom_paint_audios/pencil_sharpener_1.mp3")

water_poure = pygame.mixer.Sound("tom_paint_audios/pencil_sharpener_1.mp3")
			# from Pencil Sharpening#
				################
				### SAVE SCREEN ###
				################
				
def save_screen():

	pygame.draw.rect(screen,BACKGROUND,pygame.Rect(0,0, screen_width,color_pallet_size + 20))
		
	pygame.draw.rect(screen,BACKGROUND,pygame.Rect(0, screen_height -  color_pallet_size * 2.7 , screen_width, color_pallet_size * 2.5))
		
	file_name = "tom_paint_saved/thomas_kitaba"
	t = time.localtime()
	date_object = datetime.date.today()
	current_time = time.strftime("%H-%M-%S", t)
	file_name = file_name + str(date_object) +str(current_time) + ".jpeg"
	
	pygame.image.save(screen, file_name)
	save_sound.play()
	
	#time.sleep(1)
	#clear()
	#redraw_pallets()

				##################
				### REDRAW SCREEN ###
				##################
	
def redrow_screen():
	
	enter_name = my_medium_font.render(" Saved with  FILE NAME", 1, NEUTRAL)
	screen.blit(enter_name,(100, 10 ))
							
	file_name_txt = my_small_font.render(str(file_name), 1,(255,0, 0))
	screen.blit(file_name_txt, (50, color_pallet_size * 0.5 + 25))
	
	time.sleep(1)
	
				##################
				### REDRAW PALLET ###
				##################
	
				##################
				#### PAINT MODE ####
				##################		
	
def paint_shapes(x,y,m,n,color):
	  # PAINT MODE
	  
	   if shape_mode_line == True:
	   	 
	   	pygame.draw.line(screen, color,  (x,y),(m,n), pen_size)
	   	
	  
	   
	   if shape_mode_rectangle == True:
	   	pass
	  	

				##################
				#### PAINT MODE####
				##################
				
				
def paint(x,y):
	  # PAINT MODE
	  if  y <= screen_height - 230 and y >= ot +  color_pallet_size:
		   if erase_mode == True:
		   	color = pygame.Rect(x , y ,  pen_size * 2, pen_size * 2)
		   	pygame.draw.rect(screen, paint_color, color)
		   if paint_mode == True:
		   	color = pygame.Rect(x , y ,  pen_size, pen_size )
		   	pygame.draw.rect(screen, paint_color, color)
		   if shape_mode_line== True:
		   	pass
		   	
	  	
	  
	  
				##################
				#### ERASE MODE ####
				##################

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

rectangle_icon = [ 330 , screen_height - 210]
circle_icon = [ 440 , screen_height - 210]
line_icon = [ 550 , screen_height - 210]

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

rectangle_icon_rect_center = [0,0]
circle_icon_rect_center = [0,0]
line_icon_rect_center = [0,0]


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

line_tool = pygame.image.load("tom_paint_objects/line_0.png")
#line  https://www.flaticon.com/free-icon/diagonal-line_815548?term=line&page=1&position=68&page=1&position=68&related_id=815548&origin=search
line_tool_l = [pygame.transform.scale(line_tool,(color_pallet_size, color_pallet_size))]

rectangle_tool= pygame.image.load("tom_paint_objects/rectangle_0.png")
#rectangle https://www.flaticon.com/free-icon/stop_545767?k=1654246244064
rectangle_tool_l = [pygame.transform.scale(rectangle_tool, (color_pallet_size, color_pallet_size))]

circle_tool = pygame.image.load("tom_paint_objects/circle_0.png")

#circle https://www.flaticon.com/premium-icon/full-moon_686755?term=circle&page=1&position=74&page=1&position=74&related_id=686755&origin=search
circle_tool_l = [pygame.transform.scale(circle_tool,(color_pallet_size, color_pallet_size))]

# RECT OBJECT FOR SHAPES
rectangle_icon_rect = pygame.Rect( rectangle_icon[0], rectangle_icon[1], color_pallet_size, color_pallet_size)

circle_icon_rect = pygame.Rect( circle_icon[0], circle_icon[1], color_pallet_size, color_pallet_size)

line_icon_rect = pygame.Rect( line_icon[0], line_icon[1], color_pallet_size, color_pallet_size)


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

# CENTER FOR SHAPES
line_icon_rect_center[0] = line_icon_rect.centerx

line_icon_rect_center[1] = line_icon_rect.centery

rectangle_icon_rect_center[0] = rectangle_icon_rect.centerx

rectangle_icon_rect_center[1] = rectangle_icon_rect.centery

circle_icon_rect_center[0] = circle_icon_rect.centerx

circle_icon_rect_center[1] = circle_icon_rect.centery
	 
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

line_icon_rect_center[0] = line_icon_rect.centerx
line_icon_rect_center[1] = line_icon_rect.centery


rectangle_icon_rect_center[0] = rectangle_icon_rect.centerx
rectangle_icon_rect_center[1] = rectangle_icon_rect.centery


circle_icon_rect_center[0] = circle_icon_rect.centerx
circle_icon_rect_center[1] = circle_icon_rect.centery

line_icon_rect_center[0] = line_icon_rect.centerx
line_icon_rect_center[1] = line_icon_rect.centery


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

# LOWER PALLET SHAPES 
#def draw_shapes_pallet(color):
#pygame.draw.rect(screen, RED , rectangle_icon_rect)

#pygame.draw.rect(screen, RED, line_icon_rect)
	
#pygame.draw.circle(screen, RED, (circle_icon_rect_center[0], circle_icon_rect_center[1]) , color_pallet_size * 0.5, 30)

screen.blit(line_tool_l[0], (line_icon[0], line_icon[1]))

screen.blit(rectangle_tool_l[0], (rectangle_icon[0], rectangle_icon[1]))

screen.blit(circle_tool_l[0], (circle_icon[0], circle_icon[1]))


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


				#######################
				#### BOX ARROUND SIZE ####
				####OF BRUSH SELECTION ####
				#######################
# =========== SELECTED SIZE ========
small_size_tool = False
middium_size_tool = True
large_size_tool = False
size_of_tool = [0,0,0]
size_of_tool[1] == 1
			
tool_x = [0]
tool_y = [0]


tool_box_big = pygame.Rect(size_icon_big[0], size_icon_big[1], color_pallet_size + 2 , color_pallet_size +2 )


tool_box_middium = pygame.Rect(size_icon_middium[0] , size_icon_middium[1], color_pallet_size + 2 , color_pallet_size +2 )


tool_box_small= pygame.Rect(size_icon_small[0],size_icon_small[1], color_pallet_size + 2 , color_pallet_size +2 )

				
#

def selected_size():
	
	if small_size_tool == True or size_of_tool[0] == 1:
		tool_x[0] = size_icon_small[0]
		tool_y[0] = size_icon_small[1]
		
	
		pygame.draw.rect(screen, BACKGROUND, tool_box_big , 2)
		pygame.draw.rect(screen, BACKGROUND, tool_box_middium , 2)

		
	if  middium_size_tool == True or size_of_tool[1] == 1:
		tool_x[0] = size_icon_middium[0]
		tool_y[0] = size_icon_middium[1]
		
		pygame.draw.rect(screen, BACKGROUND, tool_box_big , 2)
		pygame.draw.rect(screen, BACKGROUND,tool_box_small, 2)
		
		
	if large_size_tool == True or size_of_tool[2] == 1:
		tool_x[0] = size_icon_big[0]
		tool_y[0] = size_icon_big[1]
		
		pygame.draw.rect(screen, BACKGROUND, tool_box_small, 2)
		pygame.draw.rect(screen, BACKGROUND, tool_box_middium , 2)
		
		
	tool_box = pygame.Rect(tool_x[0], tool_y[0], color_pallet_size + 2 , color_pallet_size +2 )
	pygame.draw.rect(screen, paint_color, tool_box , 2)
	

				#######################
				#### BOX ARROUND TYPE####
				####OF SHAPE SELECTED ####
				#######################
# =========== SELECTED SIZE ========
line_tool_bool = True
rectangle_tool_bool = False
circle_tool_bool = False

size_of_shape_tool = [0,0,0]

size_of_shape_tool[2] == 1
			
shape_x = [0]
shape_y = [0]

rectangle_icon_rect = pygame.Rect( rectangle_icon[0], rectangle_icon[1], color_pallet_size, color_pallet_size)

circle_icon_rect = pygame.Rect( circle_icon[0], circle_icon[1], color_pallet_size, color_pallet_size)

line_icon_rect = pygame.Rect( line_icon[0], line_icon[1], color_pallet_size, color_pallet_size)

rectangle_icon = [ 330 , screen_height - 210]
circle_icon = [ 440 , screen_height - 210]
line_icon = [ 550 , screen_height - 210]


def selected_shape():
	
	if line_tool_bool == True or size_of_shape_tool[0] == 1:
		
		shape_x[0] = line_icon[0]
		shape_y[0] = line_icon[1]
	
	
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, circle_icon_rect , 3)

		
	if  rectangle_tool_bool== True or size_of_tool[1] == 1:
		shape_x[0] = rectangle_icon[0]
		shape_y[0] = rectangle_icon[1]
		
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, circle_icon_rect , 3)
		
		
	if circle_tool_bool == True or size_of_tool[2] == 1:
		shape_x[0] = circle_icon[0]
		shape_y[0] = circle_icon[1]
	
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect , 2)
		
		
	tool_box = pygame.Rect(shape_x[0], shape_y[0], color_pallet_size  , color_pallet_size )
	pygame.draw.rect(screen, paint_color, tool_box , 2)
	
	if paint_mode == True:
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect , 2)
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect , 2)


				#######################
				##SHOW PAINT COLOR ON TOP##
				#######################
def show_paint_color(color):
	pygame.draw.circle(screen, color, (what_color_coord[0] + color_pallet_size * 0.5, what_color_coord[1] + color_pallet_size * 0.5) , color_pallet_size * 0.5, 20)

				#################
				#######CLEAR######
				#################
				
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
	
	screen.blit(line_tool_l[0], (line_icon[0], line_icon[1]))

	screen.blit(rectangle_tool_l[0], (rectangle_icon[0], rectangle_icon[1]))

	screen.blit(circle_tool_l[0], (circle_icon[0], circle_icon[1]))
	
	pygame.draw.line(screen, BACKGROUND,  (shape_coordinate[0], shape_coordinate[1]), (shape_coordinate[2], shape_coordinate[3]), pen_size)

# REDRAW SCREEN 
def redraw_pallets():
	
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
	
	screen.blit(line_tool_l[0], (line_icon[0], line_icon[1]))

screen.blit(rectangle_tool_l[0], (rectangle_icon[0], rectangle_icon[1]))

screen.blit(circle_tool_l[0], (circle_icon[0], circle_icon[1]))

#======== SET BRUSH SIZE
def set_paint_size():
	if paint_mode:

		SMALL = 2
		MIDDIUM = 4
		BIG = 6
		selected_size()
	
	elif shape_mode_line == True:

		SMALL = 2
		MIDDIUM = 4
		BIG = 8
		selected_size()
		
	if shape_mode_circle:

		SMALL = 2
		MIDDIUM = 4
		BIG = 6
		selected_size()
	




	# ACCTUALLY SAVE THE SCREEN

# SAVE FILE NAME NAME NAME NAME	 
file_name_l = []
	 			 	 
#	if detail == 1: display small list.
#if detail == 2 display large list
				#################
				#######GAME######
				#######START######
				#################
#

running = True
while running:
	#clock.tick(2000)
	current_time[0] = pygame.time.get_ticks()
	
	#screen.fill((0,0,0))
	#current_time = pygame.time.get_ticks()
	
	

	
	
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
			
			
			distance_with_rectangle_icon = int(math.sqrt((rectangle_icon_rect_center[0] - mousex)**2 + (rectangle_icon_rect_center[1] - mousey)**2))
			distance_with_circle_icon = int(math.sqrt((circle_icon_rect_center[0] - mousex)**2 + (circle_icon_rect_center[1] - mousey)**2))
			
			distance_with_line_icon = int(math.sqrt((line_icon_rect_center[0] - mousex)**2 + (line_icon_rect_center[1] - mousey)**2))
			
			
			
# DISTANCE WITH UPPER ICONS

# save_coord_center[1] =  color_yellow.centery
#new_coord_center[0] = color_white.centerx
#what_color_coord_center[0] = color_blue.cente

			distance_with_save = int(math.sqrt((save_coord_center[0] - mousex)**2 + (save_coord_center[1] - mousey)**2))
			
			distance_with_new = int(math.sqrt((new_coord_center[0] - mousex)**2 + (new_coord_center[1] - mousey)**2))
			
			distance_with_what_color = int(math.sqrt((what_color_coord_center[0] - mousex)**2 + (what_color_coord_center[1] - mousey)**2))
			
			distance_with_shapes = int(math.sqrt((shapes_coord_center[0] - mousex)**2 + (shapes_coord_center[1] - mousey)**2))
			
			distance_with_color_board= int(math.sqrt((paint_coord[0] - mousex)**2 + (paint_coord[1] - mousey)**2))
			
			
			if distance_with_green <= color_pallet_size * 0.5:
				#erase_mode = False
				# paint_mode = True
				set_paint_size()
			
				paint_color = GREEN
				selected_size()
				paint_drop_sound.play()
				
			if distance_with_red <= color_pallet_size * 0.5:
				erase_mode = False
				paint_mode = True	
				paint_color = RED
				selected_size()
				paint_drop_sound.play()
				
			if distance_with_yellow <= color_pallet_size * 0.5:
				#erase_mode = False
				#paint_mode = True
				
				set_paint_size()
				
				paint_color = YELLOW
				selected_size()
				
				paint_drop_sound.play()
				
			if distance_with_neutral <= color_pallet_size * 0.5:
				#erase_mode = False
				#paint_mode = True	
				
				set_paint_size()
				paint_color = NEUTRAL # white or black
				selected_size()
				paint_drop_sound.play()
			
			if distance_with_blue <= color_pallet_size * 0.5:
				#erase_mode = False
				#paint_mode = True	
				set_paint_size()
				
				paint_color = BLUE
				selected_size()
				paint_drop_sound.play()
			
			if distance_with_erasor <= color_pallet_size * 0.5 + 10:
				
				distance_with_erasor_global[0] = distance_with_erasor
				erase_mode = True
				paint_mode = False
				shape_mode_line = False
				shape_mode_rectangle = False
				shape_mode_circle= False
				
				paint_color = BACKGROUND
				#clear()
				#erase(mousex, mousey)
				
			if distance_with_size_small <= color_pallet_size :
				size_of_tool[0] == 1
				size_of_tool[1] == 0
				size_of_tool[2] == 0
				
				small_size_tool = True
				middium_size_tool = False
				large_size_tool = False
				
				pen_size = SMALL
				set_paint_size()
				#selected_size()
				pencil_sharpener.play()
				
			if distance_with_size_middium <= color_pallet_size:
				size_of_tool[0] == 0
				size_of_tool[1] == 1
				size_of_tool[2] == 0
				
				small_size_tool = False
				middium_size_tool = True
				large_size_tool = False

				
				pen_size = MIDDIUM
				set_paint_size()
				#selected_size()
				pencil_sharpener.play()
				
			if distance_with_size_big <= color_pallet_size:
				
				size_of_tool[0] == 0
				size_of_tool[1] == 0
				size_of_tool[2] == 1
				
				small_size_tool = False
				middium_size_tool = False
				large_size_tool = True
				
				pen_size = BIG
				set_paint_size()
				
			#	selected_size()
				pencil_sharpener.play()
				
			if distance_with_rectangle_icon <= color_pallet_size:
				
				size_of_shape_tool[0] == 1
				size_of_shape_tool[1] == 0
				size_of_shape_tool[2] == 0
				
				
				rectangle_tool_bool = True
				line_tool_bool= False
				circle_tool_bool = False
				
				
				#pen_size = BIG
				selected_shape()
				pencil_sharpener.play()
				
			if distance_with_circle_icon <= color_pallet_size:
				
				size_of_shape_tool[0] == 0
				size_of_shape_tool[1] == 1
				size_of_shape_tool[2] == 0
				
				
				rectangle_tool_bool = False
				circle_tool_bool = True
				line_tool_bool= False
				
				
				#pen_size = BIG
				selected_shape()
				pencil_sharpener.play()
				
			if distance_with_line_icon <= color_pallet_size:
				
				if cleared == True:
					
					#shape_coordinate.clear()
					#paint_coordinate.clear()
					paint_coordinate[0][0] = shape_coordinate[0]
					paint_coordinate[0][1] = shape_coordinate[1]
					cleared = False
				
					
					
				paint_coordinate.clear()
				erase_mode = False
				paint_mode = False
				shape_mode_line = True
				shape_mode_rectangle = False
				shape_mode_circle = False
				
				
				size_of_shape_tool[0] == 0
				size_of_shape_tool[1] == 0
				size_of_shape_tool[2] == 1
				
				
				rectangle_tool_bool = False
				circle_tool_bool = False
				line_tool_bool= True
				
				
				#pen_size = BIG
				selected_shape()
				pencil_sharpener.play()
				
				#distance_with_rectangle_icon
			# UPPER PALLET ICON CLICKED
			# save jpeg format
			if distance_with_save <= color_pallet_size:
				save_screen()
				save_mode[0] = 1
				#shape_coordinate.clear()
				#paint_coordinate.clear()
				redraw_pallets()
			if event.type == pygame. MOUSEBUTTONUP:
				pass
				save_mode[0] = 0
				
			if distance_with_new <= color_pallet_size:
				#clear = True
				
				paper_rustle.play()
				#shape_coordinate.clear()
				#paint_coordinate.clear()
				clear()
				cleared = True
				#shape_mode_line = True
				
			if distance_with_what_color <= color_pallet_size:
				erase_mode = False
				paint_mode = True
				shape_mode_line = False
				shape_mode_rectangle = False
				shape_mode_circle= False
			
			if distance_with_shapes <= color_pallet_size:
				
				erase_mode = False
				paint_mode = False
				shape_mode_line = True
				shape_mode_rectangle = False
				shape_mode_circle= False
				
				
				#shapes_rolling.play()
			
			if distance_with_color_board <= color_pallet_size:
				
				erase_mode = False
				paint_mode = True
				shape_mode_line = False
				shape_mode_rectangle = False
				shape_mode_circle= False
				
				selected_shape()
				#shapes_rolling.play()
				

				
		if pygame.mouse.get_pressed()[0]:
			
			#r
			mousex, mousey = pygame.mouse.get_pos()
			
			#if shape_mode_line == True or
			#shape_mode_rectangle = True:
				#shape_coordinate[0] = mousex
				#shape_coordinate[1] = mousey			
				
			if save_mode[0] == 1:
				
				redraw_pallets()
				time.sleep(1)
				save_mode[0] = 0
				
			if save_mode[0] == 0:
				#r
			
				show_paint_color(paint_color)
				#for i  in pen_position:
					#paint(i[0],i[1])
				paint(mousex,mousey)
			
		if event.type == pygame. MOUSEBUTTONUP:
			pass
					
			
				#paint_color = RED
			#	for i in paint_coordinate:
					#paint(i[0], i[1])
			
			save_mode[0] = 0
			
		
		if pygame.mouse.get_pressed()[0] and paint_mode ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
				#paint_coordinate.append([mousex,mousey])
				
			mousex, mousey = pygame.mouse.get_pos()
			shape_coordinate[0] = mousex
		
			shape_coordinate[1] = mousey		
				
		if pygame.mouse.get_pressed()[0] and shape_mode_line ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
				paint_coordinate.append([mousex,mousey])
				
				s_o_p_c = len(paint_coordinate)
				if s_o_p_c >1:
					shape_coordinate[0] = paint_coordinate[s_o_p_c - 1][0]
					shape_coordinate[1] = paint_coordinate[s_o_p_c - 1][1]
					
			
				if s_o_p_c <= 1:
				
					shape_coordinate[0] = paint_coordinate[0][0]
					shape_coordinate[1] = paint_coordinate[0][1]
				
				
					
					shape_coordinate[2] = paint_coordinate[s_o_p_c - 1][0]
					shape_coordinate[3] = paint_coordinate[s_o_p_c - 1][1]
				
		#if cleared == True:
			
			#paint_shapes(shape_coordinate[0], shape_coordinate[1], shape_coordinate[2], shape_coordinate[3], BACKGROUND)
			
		
		#else:
	
				paint_shapes(shape_coordinate[0], shape_coordinate[1], shape_coordinate[2], shape_coordinate[3], paint_color)
			#cleared = False
		#paint_shapes(0,0,100,100, RED)
				
		#draw_shapes_pallet(paint_color)
		#color_pallate()
	#selected_shape()
	pygame.display.update()
				
	
				
	
	
#paint_coordinate_line_cont = []