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
BEIGE = ( 245,245,220)
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

paint_coordinate_line_continious = []
shape_coordinate_line_continious = [0,0,0,0]

paint_coordinate_rectangle= []
shape_coordinate_rectangle  = [0,0,0,0]
rectangle_coordinate_backup = []

paint_coordinate_circle = []
shape_coordinate_circle  = [0,0,0,0]
circle_coordinate_backup = []

paint_coordinate_pen= []
shape_coordinate_pen = [0,0,0,0,0]


circle_pen = [0,0]

screen.fill(BACKGROUND)

#-----------------------------------------------

erase_mode = False
paint_mode = False
shape_mode_line = False
pen_mode= True  #### DEFAULT MODE
shape_mode_line_continious = False
shape_mode_rectangle= False
shape_mode_circle = False
shape_mode_circle_continious = False
line_tool_cont_bool= False


clear = False

SMALL = 3
MIDDIUM = 8
BIG = 16


pen_size = SMALL
erasor_size = pen_size * 2

current_time = [0]
save_time = [0]

save_mode = False
save_mode = [0]

cleared = False # when NEW is clicked cleared is TRUE

undo_coordinate = []
collected_undo_coordinate = []
undo_size = 0
undo_color = paint_color

#------- PALLETS -----
ot = 10 # offset from top
ob = 10 # offset from bottom
# color palett coordinates
red_coord = [ 0 , screen_height - 100  ]
green_coord = [ 110 , screen_height - 100  ]
yellow_coord = [ 220 , screen_height - 100  ]
white_coord = [ 330 , screen_height - 100  ]
blue_coord = [ 440 , screen_height - 100  ]


#---- 
#UPPER PALLET

paint_coord = [ color_pallet_size * 0 + 30 , ot  ]
shape_coord = [ color_pallet_size * 1 + 2 * 30 , ot ]
save_coord = [ color_pallet_size * 2 + 3 * 30, ot ]
erasor_coord = [ color_pallet_size * 3 + 4 * 30, ot ]
new_coord = [ color_pallet_size * 4 + 5 * 30, ot ]
what_color_coord = [ color_pallet_size *5 + 6 * 30, ot ]


#size setting coordinates pallet

size_icon_small = [ 10 , screen_height - 210  ]
size_icon_middium = [ 110 , screen_height - 210  ]
size_icon_big = [ 220 , screen_height - 210]

rectangle_icon = [ 330 , screen_height - 210]
circle_icon = [ 440 , screen_height - 210]
line_icon = [ 550 , screen_height - 210]
pen_icon = [ 660 , screen_height - 210]

line_icon_cont= [ 600 , screen_height - 100]

#%%%%%%%%%%%%%%%%%%%%%
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
				### REDRAW SCREEN ##
				##################
	
def redrow_screen():
	
	enter_name = my_medium_font.render(" Saved with  FILE NAME", 1, NEUTRAL)
	screen.blit(enter_name,(100, 10 ))
							
	file_name_txt = my_small_font.render(str(file_name), 1,(255,0, 0))
	screen.blit(file_name_txt, (50, color_pallet_size * 0.5 + 25))
	
	time.sleep(1)
	
	
	
				##################
				### UNDO LAST ACTION  ###
				##################
				
undo_coordinate = []
undo_circle_coordinate = []
undo_rectangle_coordinate = []
undo_line_coordinate = []
undo_cont_line_coordinate = []
undo_cont_circle_coordinate = []


collected_undo_coordinate = []
undo_size = 0
undo_color = paint_color

pixels_to_undo = [10]

def undo ( ):
	
	last_index = len(collected_undo_coordinate) - 1
	
	for i in range ( 1,len(collected_undo_coordinate[last_index])):
		#screen.set_at ((last_coordinate[i][0], last_coordinate[i][0]), BACKGROUND )
		pygame.draw.line(screen, BACKGROUND,  (collected_undo_coordinate[last_index][i][0],collected_undo_coordinate[last_index][i][1]),(collected_undo_coordinate[last_index][i][2],collected_undo_coordinate[last_index][i][3]), collected_undo_coordinate[last_index][i][4])	
		
		
def undo_last_paint ( last_coordinate ):
	
	if len(last_coordinate ) > 0:
	
		for i in range (len(last_coordinate) - pixels_to_undo[0], len(last_coordinate)):
			#screen.set_at ((last_coordinate[i][0], last_coordinate[i][0]), BACKGROUND )
			pygame.draw.line(screen, BACKGROUND,  (last_coordinate[i][0],last_coordinate[i][1]),(last_coordinate[i][2],last_coordinate[i][3]), undo_size)
		#undo_coordinate.remove(undo_coordinate(i))

def  undo_last_cont_line(a):
	
	for i in range (len(undo_cont_line_coordinate) - pixels_to_undo[0], len(undo_cont_line_coordinate)):
		
		
		pygame.draw.line(screen, BACKGROUND,  (a[i][0], a[i][1]), (a[i][2], a[i][3]), undo_size)	
			
def undo_last_cont_circle(c):
		# NOT FINISJED YET
				
			pygame.draw.circle(screen, BACKGROUND , (c[i][0],  c[i][1] , c[i][2]) , paint_size)
				
				
def undo_last_circle(c):
			
			#for i in range(len(c)):
			i = len(c) - 1	
			if len(c) -1 > 0:
				pygame.draw.circle(screen, BACKGROUND , (c[i][0],  c[i][1] ), c[i][2], pen_size)
		
				c.pop(len(c)-1)	
def  undo_last_rectangle(r):
 	j = len(r)- 1
 	if j > 0:
	 	rectangle =  pygame.Rect(r[j][0], r[j][1], r[j][2], r[j][3])
	 	pygame.draw.rect(screen,BACKGROUND,rectangle,pen_size)
	 	r.pop(j)
			

def  undo_last_line(a):
		pass
		
#+++++++++++++++++++++++++++++
	
				##################
				#### SHAPE MODE ####
				##################		


shape_continious_line = [0,0,0,0]
paint_continious_line = [ ]


#.====CONTINIUS LINE ====
def paint_continious_line(x,y,m,n,color):
	pygame.draw.line(screen, color,  (x,y),(m,n), pen_size)
#===== PEN ====
def paint_like_pen(x,y,m,n,color,size): # paint gojo line
	pygame.draw.line(screen, color,  (x,y),(m,n), size)		

#===== LINE =====
def paint_shapes(x,y,m,n,color): # paint gojo line
	  # PAINT MODE
	  
	   if shape_mode_line == True:
	   	pygame.draw.line(screen, color,  (x,y),(m,n), pen_size)
	   	redraw_pallets()
	 #  if shape_mode_line_continious == True:
	 
	   #	pygame.draw.line(screen, color,  (x,y),(m,n), pen_size)
	   if shape_mode_rectangle == True:
	   	pygame.draw.line(screen, color,  (0,100),(400,400), pen_size)
	   	# ======RECTANGLE=======
def paint_rectangle(x, y, m, n, color, size):
 	rectangle =  pygame.Rect(x,y, m, n)
 	pygame.draw.rect(screen,color,rectangle,size)
 	
 # ==== CIRCLE  ====
 

def paint_circle(x, y, r, color,size):
	#if  y <= screen_height - 230 and y >= ot +  color_pallet_size:
		pygame.draw.circle(screen, color, (x , y) , r, size)
		redraw_pallets()
	#paint_circle(x, y, r, paint_color,pen_size)

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
	 erasor_color = pygame.Rect(x , y ,  erasor_size+ 4, erasor_size + 4 )
	 pygame.draw.rect(screen, BACKGROUND, erasor_color)


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
line_icon_cont_rect_center = [0,0]
pen_icon_rect_center = [0,0]


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

circle_tool = pygame.image.load("tom_paint_objects/center_circle.png")



overlapping_circles_tool = pygame.image.load("tom_paint_objects/overlapping_circles_1.png")

overlapping_circles_tool_l = [pygame.transform.scale(overlapping_circles_tool,(color_pallet_size, color_pallet_size))]

pencil_tool = pygame.image.load("tom_paint_objects/pencil_1.png")

pencil_tool_l = [pygame.transform.scale(pencil_tool, (color_pallet_size, color_pallet_size))]

continious_pencil_tool = pygame.image.load("tom_paint_objects/pencil_continious_1.png")

continious_pencil_tool_l = [pygame.transform.scale(continious_pencil_tool, (color_pallet_size, color_pallet_size))]


#circle https://www.flaticon.com/premium-icon/full-moon_686755?term=circle&page=1&position=74&page=1&position=74&related_id=686755&origin=search
circle_tool_l = [pygame.transform.scale(circle_tool,(color_pallet_size, color_pallet_size))]

# RECT OBJECT FOR SHAPES
rectangle_icon_rect = pygame.Rect( rectangle_icon[0], rectangle_icon[1], color_pallet_size, color_pallet_size)

circle_icon_rect = pygame.Rect( circle_icon[0], circle_icon[1], color_pallet_size, color_pallet_size)


line_icon_rect = pygame.Rect( line_icon[0], line_icon[1], color_pallet_size, color_pallet_size)

line_icon_cont_rect = pygame.Rect( line_icon_cont[0], line_icon_cont[1], color_pallet_size, color_pallet_size)


pen_icon_rect = pygame.Rect( pen_icon[0], pen_icon[1], color_pallet_size, color_pallet_size)
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

line_icon_cont_rect_center[0] = line_icon_cont_rect.centerx

line_icon_cont_rect_center[1] = line_icon_cont_rect.centery

pen_icon_rect_center [0] = pen_icon_rect.centerx

pen_icon_rect_center [1] = pen_icon_rect.centery


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


#BOTTOM

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

#screen.blit(circle_tool_l[0], (circle_icon[0], circle_icon[1]))

#pygame.draw.rect(screen, (100,100,100) , line_icon_cont_rect)

#pygame.draw.rect(screen, (100,0,100) , pen_icon_rect)

screen.blit(continious_pencil_tool_l[0], (line_icon_cont[0], line_icon_cont[1]))

screen.blit(pencil_tool_l[0], (pen_icon[0], pen_icon[1]))

screen.blit(overlapping_circles_tool_l[0], (blue_coord[0], blue_coord[1]))

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
pen_tool_bool = False
line_tool_cont_bool = False
rectangle_tool_bool = False
circle_tool_bool = False
circle_tool_cont_bool = False
		

size_of_shape_tool = [0,0,0,0,0,0]
# 1= rectangle
#2= circle
#3= line 
#4= continious line

size_of_shape_tool[2] == 1
			
shape_x = [0]
shape_y = [0]

rectangle_icon_rect = pygame.Rect( rectangle_icon[0], rectangle_icon[1], color_pallet_size, color_pallet_size)

circle_icon_rect = pygame.Rect( circle_icon[0], circle_icon[1], color_pallet_size, color_pallet_size)

line_icon_rect = pygame.Rect( line_icon[0], line_icon[1], color_pallet_size, color_pallet_size)

pen_icon_rect = pygame.Rect( pen_icon[0], pen_icon[1], color_pallet_size, color_pallet_size)

rectangle_icon = [ 330 , screen_height - 210]
circle_icon = [ 440 , screen_height - 210]
line_icon = [ 550 , screen_height - 210]


def selected_shape():
	
	if line_tool_bool == True or size_of_shape_tool[0] == 1:
		
		shape_x[0] = line_icon[0]
		shape_y[0] = line_icon[1]
	
	
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, circle_icon_rect , 3)
		pygame.draw.rect(screen, BACKGROUND, line_icon_cont_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, pen_icon_rect, 3)
		
	if line_tool_cont_bool == True or size_of_shape_tool[3] == 1:
		
		shape_x[0] = line_icon_cont[0]
		shape_y[0] = line_icon_cont[1]
	
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, circle_icon_rect , 3)	
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, pen_icon_rect, 3)

		
	if  rectangle_tool_bool== True :#or  size_of_shape_tool[1] == 1:
		shape_x[0] = rectangle_icon[0]
		shape_y[0] = rectangle_icon[1]
		
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 3)
		
		pygame.draw.rect(screen, BACKGROUND, circle_icon_rect , 3)
		
		pygame.draw.rect(screen, BACKGROUND, line_icon_cont_rect, 3)
		
		pygame.draw.rect(screen, BACKGROUND, pen_icon_rect, 3)
			
	if circle_tool_bool == True or size_of_tool[2] == 1:
		shape_x[0] = circle_icon[0]
		shape_y[0] = circle_icon[1]
	
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect , 2)
		pygame.draw.rect(screen, BACKGROUND, line_icon_cont_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, pen_icon_rect, 3)
		
		
	tool_box = pygame.Rect(shape_x[0], shape_y[0], color_pallet_size  , color_pallet_size )
	pygame.draw.rect(screen, paint_color, tool_box , 2)
	
	if paint_mode == True:
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect , 2)
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect , 2)
		pygame.draw.rect(screen, BACKGROUND, line_icon_cont_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, pen_icon_rect, 3)
		
	#tool_box = pygame.Rect(shape_x[0], shape_y[0], color_pallet_size , color_pallet_size  )
	#pygame.draw.rect(screen, paint_color, tool_box , 2)
	
	if pen_mode == True:
		shape_x[0] = pen_icon[0]
		shape_y[0] = pen_icon[1]
		
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect , 2)
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect , 2)
		pygame.draw.rect(screen, BACKGROUND, line_icon_cont_rect, 3)
	
	if shape_mode_line_continious == True:
		shape_x[0] = line_icon_cont[0]
		shape_y[0] = line_icon_cont[1]
		
		pygame.draw.rect(screen, BACKGROUND, line_icon_rect, 2)
		pygame.draw.rect(screen, BACKGROUND, rectangle_icon_rect , 2)
		
		pygame.draw.rect(screen, BACKGROUND, pen_icon_rect, 3)
		pygame.draw.rect(screen, BACKGROUND, line_icon_cont_rect, 3)
	
		
		
		#shape_mode_line_continious = False line_icon_cont_rect
		
	tool_box = pygame.Rect(shape_x[0], shape_y[0], color_pallet_size , color_pallet_size  )
	pygame.draw.rect(screen, paint_color, tool_box , 2)

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
	selected_shape()
	selected_size()
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
	
	# behind line_icon_cont_rect
	#pygame.draw.rect(screen, (100,100,100), line_icon_cont_rect, 3)
	# behind
#	pygame.draw.rect(screen, (100,100,100) , line_icon_cont_rect)
	# behind pen_icon_rect
	#pygame.draw.rect(screen, (100,0,100) , pen_icon_rect)
	
	
	screen.blit(continious_pencil_tool_l[0], (line_icon_cont[0], line_icon_cont[1]))

	screen.blit(pencil_tool_l[0], (pen_icon[0], pen_icon[1]))

	screen.blit(overlapping_circles_tool_l[0], (blue_coord[0], blue_coord[1]))
	
	pygame.draw.line(screen, BACKGROUND,  (shape_coordinate[0], shape_coordinate[1]), (shape_coordinate[2], shape_coordinate[3]), pen_size)
	
	paint_coordinate_line_continious.clear()

# REDRAW SCREEN 

def redraw_pallets():
	
	tools_back_top = pygame.Rect(0,  0, screen_width,  color_pallet_size + 20 )
		
	pygame.draw.rect(screen, BACKGROUND, tools_back_top)
		
	tools_back_bottom = pygame.Rect(0, screen_height - color_pallet_size * 2.7, screen_width,  color_pallet_size + 200 )
	
	pygame.draw.rect(screen, BACKGROUND, tools_back_bottom)
	selected_shape()
	selected_size()
	
	pygame.draw.rect(screen, RED, color_red)
	pygame.draw.rect(screen, GREEN, color_green)
	pygame.draw.rect(screen,YELLOW , color_yellow)
	pygame.draw.rect(screen, NEUTRAL , color_white)
	pygame.draw.rect(screen, BLUE , color_blue)
	
	#====
	screen.blit(rectangle_tool_l[0], (rectangle_icon[0], rectangle_icon[1]))

	screen.blit(circle_tool_l[0], (circle_icon[0], circle_icon[1]))
	pygame.draw.rect(screen, (100,100,100), line_icon_cont_rect, 3)
	
	pygame.draw.rect(screen, (100,100,100) , line_icon_cont_rect)
	
	pygame.draw.rect(screen, (100,0,100) , pen_icon_rect)
	
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

	screen.blit(continious_pencil_tool_l[0], (line_icon_cont[0], line_icon_cont[1]))

	screen.blit(pencil_tool_l[0], (pen_icon[0], pen_icon[1]))

	screen.blit(overlapping_circles_tool_l[0], (blue_coord[0], blue_coord[1]))

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

#================================
				#######GAME######
				#######SETTING####
				#################			
def  start_screen( ):
		
		
		view_setting = True
		
		while view_setting :
			#screen.fill(BACKGROUND)
			pygame.draw.rect(screen, RED, pygame.Rect( 0, 0,  screen_width, screen_height))
			
			for event in pygame.event.get():
	 	
	 			if event.type == pygame. MOUSEBUTTONDOWN:
			 		view_setting =False
			 	
#start_screen()
paint_color = YELLOW
selected_size()
selected_shape() # SHOW DEFAULT COLOUR				
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 			 	 
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
			
			distance_with_pen_icon = int(math.sqrt((pen_icon_rect_center[0] - mousex)**2 + (pen_icon_rect_center[1] - mousey)**2))
			
			distance_with_line_icon_cont = int(math.sqrt((line_icon_cont_rect_center[0] - mousex)**2 + (line_icon_cont_rect_center[1] - mousey)**2))
		
			
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
				
				set_paint_size()
			
				paint_color = GREEN
				selected_size()
				selected_shape()
				paint_drop_sound.play()
				
			if distance_with_red <= color_pallet_size * 0.5:
				erase_mode = False
				
				paint_color = RED
				
				selected_size()
				selected_shape()
				paint_drop_sound.play()
				
				
			if distance_with_yellow <= color_pallet_size * 0.5:
				
				erase_mode = False
				set_paint_size()
				
				paint_color = YELLOW
				selected_size()
				selected_shape()
				
				paint_drop_sound.play()
				
			if distance_with_neutral <= color_pallet_size * 0.5:
				#erase_mode = False
				#paint_mode = True	
				
				set_paint_size()
				paint_color = NEUTRAL # white or black
				selected_size()
				selected_shape()
				
			
				paint_drop_sound.play()
			
		# BACKUP USED TO TEST UNDO AND REDO
			if distance_with_blue <= color_pallet_size * 0.5:
				pass
				
	#$$$$$$$$$$$$$$$BACKUP CODE $$$$$$$$$$
#	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
			#if distance_with_blue <= color_pallet_size * 0.5:
				
				#set_paint_size()
				
				#paint_color = BLUE
				#selected_size()
				#selected_shape()
				#paint_drop_sound.play()
				
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
			
			if distance_with_blue <= color_pallet_size * 0.5:
				pass
				
				
			
			if distance_with_erasor <= color_pallet_size * 0.5 + 10:
				#mousex,mousey = pygame.mouse.get_pressed()
				distance_with_erasor_global[0] = distance_with_erasor
				erase_mode = True
				paint_mode = False
				#shape_mode_line = False
				#shape_mode_rectangle = False
				#shape_mode_circle= False
				selected_shape()
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
			#	set_paint_size()
				selected_size()
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
				selected_size()
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
				
				selected_size()
				pencil_sharpener.play()
				
			if distance_with_rectangle_icon <= color_pallet_size:
				if len(paint_coordinate_rectangle) > 1:
					paint_coordinate_rectangle.clear()
				
				size_of_shape_tool[0] = 1
				size_of_shape_tool[1] = 0
				size_of_shape_tool[2] = 0
				size_of_shape_tool[3] = 0
				size_of_shape_tool[4] = 0
				size_of_shape_tool[5] = 0
				
				erase_mode = False
				paint_mode = False
				shape_mode_line = False
				shape_mode_line_continious = False
				shape_mode_rectangle = True
				shape_mode_circle = False
				pen_mode = False
				
				
				rectangle_tool_bool = True
				line_tool_bool= False
				pen_tool_bool = False
				circle_tool_bool = False
				circle_tool_cont_bool = False
				line_tool_cont_bool = False
				
				
				#pen_size = BIG
				selected_shape()
				pencil_sharpener.play()
				
		
			if distance_with_circle_icon <= color_pallet_size:
				#if len(shape_coordinate_circle) > 1:
				#	shape_coordinate_circle.clear()
				
				paint_coordinate_circle.clear()
				erase_mode = False
				paint_mode = False
				pen_mode = False
				shape_mode_line = False
				shape_mode_line_continious = False
				shape_mode_rectangle = False
				shape_mode_circle_continious = False
				shape_mode_circle = True
				
				
				size_of_shape_tool[0] = 0
				size_of_shape_tool[1] = 1
				size_of_shape_tool[2] = 0
				size_of_shape_tool[3] = 0
				size_of_shape_tool[4] = 0
				size_of_shape_tool[5] = 0
				
				
				rectangle_tool_bool = False
				circle_tool_bool = True
				circle_tool_cont_bool
				line_tool_bool= False
				pen_tool_bool = False
				line_tool_cont_bool = False
				
				#pen_size = BIG
				selected_shape()
				pencil_sharpener.play()
				
			if distance_with_line_icon <= color_pallet_size:
				
				if shape_mode_line_continious == True:
					shape_coordinate[0] = 0
					shape_coordinate[1] = 0
				
				#if cleared == True:
					
					#shape_coordinate.clear()
					#paint_coordinate.clear()
					#paint_coordinate[0][0] =0 #shape_coordinate[0]
					#paint_coordinate[0][0] = 0 #shape_coordinate[0]
					#cleared = False
					
				paint_coordinate.clear()
				
				erase_mode = False
				paint_mode = False
				shape_mode_line = True
				pen_mode = False
				shape_mode_rectangle = False
				shape_mode_circle = False
				shape_mode_circle_continious = False
				shape_mode_line_continious = False
				
				
				size_of_shape_tool[0] == 0
				size_of_shape_tool[1] == 0
				size_of_shape_tool[2] == 1
				size_of_shape_tool[3] == 0
				size_of_shape_tool[4] == 0
				size_of_shape_tool[5] = 0
				
				
				rectangle_tool_bool = False
				circle_tool_bool = False
				circle_tool_cont_bool = False
				line_tool_bool= True
				pen_tool_bool = False
				line_tool_cont_bool = False
				
				
				#pen_size = BIG
				selected_shape()
				pencil_sharpener.play()
				
				#distance_with_rectangle_icon
			# UPPER PALLET ICON CLICKED
			# save jpeg format
			if distance_with_pen_icon <= color_pallet_size:
				
				if len(paint_coordinate_pen) > 1:
					paint_coordinate_pen.clear()
					
				size_of_shape_tool[0] = 0
				size_of_shape_tool[1] = 0
				size_of_shape_tool[2] = 0
				size_of_shape_tool[3] = 0
				size_of_shape_tool[4] = 1
				size_of_shape_tool[5] = 0
				
				rectangle_tool_bool = False
				line_tool_bool= False
				circle_tool_bool = False
				line_tool_cont_bool = False
				pen_tool_bool = True
				circle_tool_cont_bool = False
				
				
				erase_mode = False
				paint_mode = False
				shape_mode_line = False
				pen_mode = True
				shape_mode_rectangle = False
				shape_mode_circle = False
				shape_mode_circle_continious = False
				shape_mode_line_continious = False
				
				
				selected_shape()
				pencil_sharpener.play()
					
			if distance_with_line_icon_cont <= color_pallet_size:
				
				if len(paint_coordinate_line_continious) > 1:
					paint_coordinate_line_continious.clear()
					
				size_of_shape_tool[0] = 0
				size_of_shape_tool[1] = 0
				size_of_shape_tool[2] = 0
				size_of_shape_tool[3] = 1
				size_of_shape_tool[4] = 0
				size_of_shape_tool[5] = 0
				
				
				rectangle_tool_bool = False
				line_tool_bool= False
				circle_tool_bool = False
				circle_tool_cont_bool = False
				line_tool_cont_bool = True
				pen_tool_bool = False
				
				
				erase_mode = False
				paint_mode = False
				shape_mode_line = False
				shape_mode_rectangle = False
				shape_mode_circle = False
				shape_mode_circle_continious = False
				shape_mode_line_continious = True
				
				
				selected_shape()
				pencil_sharpener.play()
				
				#paint_shapes (0,600, 600,600,paint_color)
#-----------------------------------------------			
			
			if distance_with_save <= color_pallet_size:
				save_screen()
				save_mode[0] = 1
				#shape_coordinate.clear()
				#shape_coordinate[0] = paint_coordinate[len(paint_coordinate) -1][0]
				#shape_coordinate[1] = paint_coordinate[len(paint_coordinate) -1][1]
				redraw_pallets()
			if event.type == pygame. MOUSEBUTTONUP:
				pass
				save_mode[0] = 0
#-----------------------------------------------				
			if distance_with_new <= color_pallet_size:
				#clear = True
				
				paper_rustle.play()
				#shape_coordinate.clear()
				paint_coordinate.clear()
				paint_coordinate_circle.clear()
				paint_coordinate_line_continious.clear()
				paint_coordinate_rectangle.clear()
				
				clear()
				cleared = True
				#shape_mode_line = True
				
#========= continious line===========				
				
	# COLOR VIEWER WILL also BE USED to UNDO last CHANGE  
				####################
				#####  VIEW COLOR    ####
				######   UNDO  #######
				###################
				
#undo_coordinate = []
#undo_circle_coordinate = []
#undo_cont_circle_coordinate = []
#undo_rectangle_coordinate = []
#undo_line_coordinate = []
#undo_cont_line_coordinate = []
				
			if distance_with_what_color <= color_pallet_size:
				
				if pen_mode :
				
					if len(undo_coordinate)  > 0:
						undo_last_paint (undo_coordinate)
						#undo( )
						#for i in range (len(undo_coordinate)-10,  len(undo_coordinate)):
						for i in range(10):
							if len(undo_coordinate)  > 0:
								undo_coordinate.pop(len(undo_coordinate) - 1)
	#--------------------------------------------	
				if shape_mode_line :
					if len(undo_line_coordinate) > 0:
						
						undo_last_line(undo_line_coordinate)
						for i in range(10):
							if len(undo_line_coordinate) >0:
								undo_line_coordinate.pop(len(undo_line_coordinate) - 1)
								
							
					
	#--------------------------------------------	
				if shape_mode_line_continious :
					if len(undo_cont_line_coordinate) >0:
						undo_last_cont_line (undo_cont_line_coordinate)
						for i in range(10):
							if len(undo_cont_line_coordinate) >0:
								undo_cont_line_coordinate.pop(len(undo_cont_line_coordinate) - 1)
						
						
						
	#--------------------------------------------	
				if shape_mode_rectangle :
					undo_last_rectangle (undo_rectangle_coordinate)
					
					if len(undo_rectangle_coordinate) > 0:
						undo_rectangle_coordinate.pop(len(undo_rectangle_coordinate) - 1)
						
	#--------------------------------------------		
				if shape_mode_circle == True:
					undo_last_circle (undo_circle_coordinate)
					
					if len(undo_circle_coordinate) > 0:
						undo_circle_coordinate.pop(len(undo_circle_coordinate) - 1)
						
				circle_coordinate_backup
				if shape_mode_circle_continious == True:
					undo_last_cont_circle (undo_circle_coordinate)
					for i in range(10):
						if len(undo_cont_circle_coordinate):
							undo_cont_circle_coordinate.pop(len(undo_cont_circle_coordinate) - 1)
						pass
					
#++++++++++++++++++++++++++++++++++++						
			if distance_with_shapes <= color_pallet_size:
				
				erase_mode = False
				#paint_mode = False#
				shape_mode_line = True
				
				#shape_mode_rectangle = False
				#shape_mode_circle= False
				#shapes_rolling.play()
			
			if distance_with_color_board <= color_pallet_size:
				
				
				if paint_mode == True:
					paint_mode = False
				if paint_mode == False:
					paint_mode = True
				#erase_mode = False
				#shape_mode_line = False
				#shape_mode_rectangle = False
				#shape_mode_circle= False
				#shape_mode_circle_continious = False
				#shape_mode_line_continious = False
				
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
				save_mode[0] = 0
				
		if pygame.mouse.get_pressed()[0] and pen_mode==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
				show_paint_color(paint_color)
				mousex,mousey = pygame.mouse.get_pos()
				#undo_coordinate.clear()
				paint_coordinate_pen.append([mousex,mousey])
				 # to send last drawn coordinate to undo paint function () append([mousex,mousey]) )

			#	undo_coordinate.clear()
				s_o_p_pen = len(paint_coordinate_pen)
				
				if s_o_p_pen ==1:
					
					shape_coordinate_pen[0] = paint_coordinate_pen[0][0]
					shape_coordinate_pen[1] = paint_coordinate_pen[0][1]
					
					shape_coordinate_pen[2] = paint_coordinate_pen[s_o_p_pen - 1][0]
					shape_coordinate_pen[3] = paint_coordinate_pen[s_o_p_pen - 1][1]
				
					
			
				if s_o_p_pen > 2:
				
					shape_coordinate_pen[0] = paint_coordinate_pen[s_o_p_pen - 2][0] # second to last  coordinate
					shape_coordinate_pen[1] = paint_coordinate_pen[s_o_p_pen - 2][1]# second to last coordinate
				
					shape_coordinate_pen[2] = paint_coordinate_pen[s_o_p_pen - 1][0]##last coordinate
					shape_coordinate_pen[3] = paint_coordinate_pen[s_o_p_pen - 1][1]
					
		shape_coordinate_pen[4] = pen_size			#paper_rustle.play()			
		x= shape_coordinate_pen[0]	
		y = shape_coordinate_pen[1]	
		p = shape_coordinate_pen[2]
		q = shape_coordinate_pen[3]
		s = shape_coordinate_pen[4]
		
		undo_color = paint_color
		undo_size = pen_size
		undo_coordinate.append([x, y , p, q, s])
		paint_like_pen(x,y,p,q, paint_color, pen_size)
		
		
#====== CONTINIOUS LINE ========		
		if pygame.mouse.get_pressed()[0] and shape_mode_line_continious ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
				
				show_paint_color(paint_color)
				mousex,mousey = pygame.mouse.get_pos()
				
				paint_coordinate_line_continious.append([mousex,mousey])
				
				s_o_p_c_cont = len(paint_coordinate_line_continious)
				
				if s_o_p_c_cont ==1:
					
					shape_coordinate_line_continious[0] = paint_coordinate_line_continious[0][0]
					shape_coordinate_line_continious[1] = paint_coordinate_line_continious[0][1]
					
					shape_coordinate_line_continious[2] = paint_coordinate_line_continious[s_o_p_c_cont - 1][0]
					shape_coordinate_line_continious[3] = paint_coordinate_line_continious[s_o_p_c_cont - 1][1]
			
				if s_o_p_c_cont > 2:
				
					shape_coordinate_line_continious[0] = paint_coordinate_line_continious[s_o_p_c_cont - 2][0] # second to last  coordinate
					shape_coordinate_line_continious[1] = paint_coordinate_line_continious[s_o_p_c_cont - 2][1]# second to last coordinate
				
					shape_coordinate_line_continious[2] = paint_coordinate_line_continious[s_o_p_c_cont - 1][0]##last coordinate
					shape_coordinate_line_continious[3] = paint_coordinate_line_continious[s_o_p_c_cont - 1][1]
					#shape_coordinate_line_continious[4]
					
					#paper_rustle.play()			
		r = shape_coordinate_line_continious[0]	
		s = shape_coordinate_line_continious[1]	
		t = shape_coordinate_line_continious[2]
		u = shape_coordinate_line_continious[3]
		#
		#s = shape_coordinate_line_continious[4]
		undo_cont_line_coordinate.append([r,s, t, u])
		paint_continious_line(r, s, t, u, paint_color)
	#	paint_shapes(x,y,p,q, paint_color)
		
	#	paint_shapes(0, 100 , 500, 100, paint_color)
			
			
		#	if  s_o_p_c_cont > 2:
	#paint_shapes(paint_coordinate_line_continious[s_o_p_c_cont - 2][0], paint_coordinate_line_continious[s_o_p_c_cont - 2][1], paint_coordinate_line_continious[s_o_p_c_cont - 1][0]  ,paint_coordinate_line_continious[s_o_p_c_cont - 1][1] , paint_color)
				
		if pygame.mouse.get_pressed()[0] and paint_mode ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
				
				#paint_coordinate.append([mousex,mousey])
				
			mousex, mousey = pygame.mouse.get_pos()
			shape_coordinate[0] = mousex
		
			shape_coordinate[1] = mousey
			
		#paint_shapes(shape_coordinate[0], shape_coordinate[1], shape_coordinate[2], shape_coordinate[3], paint_color)
		
#=========  RECTANGLE =============
		if pygame.mouse.get_pressed()[0] and shape_mode_rectangle ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
			
			show_paint_color(paint_color)
			mousex,mousey = pygame.mouse.get_pos()
			paint_coordinate_rectangle.append([mousex,mousey])
			
			s_o_p_r = len(paint_coordinate_rectangle)
			
			shape_coordinate_rectangle[0] = paint_coordinate_rectangle[0][0]
			
			shape_coordinate_rectangle[1] = paint_coordinate_rectangle[0][1]
			
			if s_o_p_r == 1:
				shape_coordinate_rectangle[2] = shape_coordinate_rectangle[0]
			
				shape_coordinate_rectangle[3] = shape_coordinate_rectangle[0]
			
			if s_o_p_r >= 2:
			 	shape_coordinate_rectangle[0] = paint_coordinate_rectangle[0][0]
			 	shape_coordinate_rectangle[1] = paint_coordinate_rectangle[0][1]
			 	shape_coordinate_rectangle[2] = paint_coordinate_rectangle[s_o_p_r - 1][0]
			 	shape_coordinate_rectangle[3] = paint_coordinate_rectangle[s_o_p_r - 1][1]
			
			start_x = 0
			start_y = 0
			width = 0
			height= 0
			orign_x= shape_coordinate_rectangle[0] 
			orign_y=shape_coordinate_rectangle[1] 
			end_x= shape_coordinate_rectangle[2] 
			end_y=shape_coordinate_rectangle[3]
			
			
			if orign_x < end_x and orign_y < end_y:
				width = end_x - orign_x
				height = end_y - orign_y
				
				start_x = orign_x
				start_y = orign_y
				
			if orign_x > end_x and orign_y > end_y:
				width =   orign_x - end_x
				height = orign_y - end_y
				
				start_x = end_x
				start_y = end_y
			
			if orign_x > end_x and orign_y < end_y:
				width = orign_x - end_x
				height = end_y - orign_y
				
				start_x = end_x
				start_y = orign_y
				
			if orign_x < end_x and orign_y > end_y:
				width = end_x - orign_x
				height =  orign_y - end_y
				
				start_x = orign_x
				start_y = end_y
			
			x = start_x
			y = start_y
			p = width
			q = height
			undo_rectangle_coordinate.append ([x, y, p, q])
			paint_rectangle(x, y, p, q, paint_color,pen_size)
#==========CIRCLE===================
		if pygame.mouse.get_pressed()[0] and shape_mode_circle ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
			
			show_paint_color(paint_color)
			mousex,mousey = pygame.mouse.get_pos()
			paint_coordinate_circle.append([mousex,mousey])
			
			s_o_p_c = len(paint_coordinate_circle)
			
			shape_coordinate_circle[0] = paint_coordinate_circle[0][0]
			shape_coordinate_circle[1] = paint_coordinate_circle[0][1]
			
			if s_o_p_c <= 1:
				
				shape_coordinate_circle[2] = shape_coordinate_circle[0]
			
				shape_coordinate_circle[3] = shape_coordinate_circle[0]
			
			if s_o_p_c > 1:	
			 
			 	shape_coordinate_circle[2] = paint_coordinate_circle[s_o_p_c - 1][0]
			 	shape_coordinate_circle[3] = paint_coordinate_circle[s_o_p_c - 1][1]
		
			
			start_x= shape_coordinate_circle[0] 
			start_y=shape_coordinate_circle[1] 
			end_x= shape_coordinate_circle[2] 
			end_y=shape_coordinate_circle[3]
			
			
			if s_o_p_c <= 1:
				radius = 0;
				
			else:
				radius = int(math.sqrt((start_x - end_x)**2 + (start_y - end_y)**2))
			
			x = start_x
			y = start_y
			r = radius
			
			# to use the orign as starting point for star line mode we assign the x,y (the center) in a global list varable circle_pen ( TO BE USED WHEN BOTH CIRCLE AND STAR LINE MODE ARE ON TOGETHER)
			#circle_pen[0] = x
			#circle_pen[1] = y
			undo_circle_coordinate.append([x, y, r])
			
			paint_circle(x, y, r, paint_color,pen_size)
					
				#############
				#### CIRCLE ###
				############
				
#==================================
		if pygame.mouse.get_pressed()[0] and shape_mode_circle_continious ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
					
					show_paint_color(paint_color)
					mousex,mousey = pygame.mouse.get_pos()
				# to hold information for UNDO
				if len(paint_coordinate_circle) > 0:
					circle_coordinate_backup = ([mousex,mousey])
				else:
					#circle_coordinate_backup= paint_coordinate_circle
					pass
				
				paint_coordinate_circle.append([mousex,mousey])
					s_o_p_c = len(paint_coordinate_circle)
					
					shape_coordinate_circle[0] = paint_coordinate_circle[0][0]
					shape_coordinate_circle[1] = paint_coordinate_circle[0][1]
					
					if s_o_p_c <= 1:
						
						shape_coordinate_circle[2] = shape_coordinate_circle[0]
					
						shape_coordinate_circle[3] = shape_coordinate_circle[0]
					
					if s_o_p_c > 1:	
					 
					 	shape_coordinate_circle[2] = paint_coordinate_circle[s_o_p_c - 1][0]
					 	shape_coordinate_circle[3] = paint_coordinate_circle[s_o_p_c - 1][1]
				
					
					start_x= shape_coordinate_circle[0] 
					start_y=shape_coordinate_circle[1] 
					end_x= shape_coordinate_circle[2] 
					end_y=shape_coordinate_circle[3]
					
					
					if s_o_p_c <= 1:
						radius = 0
						
					else:
						radius = int(math.sqrt((start_x - end_x)**2 + (start_y - end_y)**2))
					
					x = start_x
					y = start_y
					r = radius
					# to use the orign as starting point for star line mode we assign the x,y (the center) in a global list varable circle_pen ( TO BE USED WHEN BOTH CIRCLE AND STAR LINE MODE ARE ON TOGETHER)
					#circle_pen[0] = x
					#circle_pen[1] = y
					
					paint_circle(x, y, r, paint_color,pen_size)		
					
	#++++++++++++++++++++++++++++++++++
	
		if pygame.mouse.get_pressed()[0] and shape_mode_line ==  True and mousey <= screen_height - 230 and mousey >= ot +  color_pallet_size:
				show_paint_color(paint_color)
				paint_coordinate.append([mousex,mousey])
				
				s_o_p_c = len(paint_coordinate)
				
				if s_o_p_c >1:
					#if shape_mode_circle== True:
						#shape_coordinate[0] = circle_pen[0]
						#shape_coordinate[1] = circle_pen[1]
					#else:
						shape_coordinate[0] = paint_coordinate[s_o_p_c - 1][0]
						shape_coordinate[1] = paint_coordinate[s_o_p_c - 1][1]
					
				if s_o_p_c <= 1:
				#if shape_mode_circle== True:
						#shape_coordinate[0] = circle_pen[0]
						#shape_coordinate[1] = circle_pen[1]
					#else:	
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
	#for event in pygame.event.get():
		
		if event.type == pygame. MOUSEBUTTONUP: 
			if pen_mode== True:
				paint_coordinate_pen.clear()
				#collected_undo_coordinate.append([undo_coordinate])
		if event.type == pygame. MOUSEBUTTONDOWN and shape_mode_circle:
			#	paint_coordinate_circle.clear()
			if shape_mode_circle:
					start_x= shape_coordinate_circle[0] 
					start_y=shape_coordinate_circle[1] 
					end_x= shape_coordinate_circle[2] 
					end_y=shape_coordinate_circle[3]
					
					paint_circle(start_x, start_y, 2, paint_color, pen_size)
					
			
				
	show_paint_color(paint_color)			
	pygame.display.update()
				
	
				
	
	
#paint_coordinate_line_cont = []