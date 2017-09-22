import pygame 
import time
import random

pygame.init()

disp_width=800
disp_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
bright_red=(200,0,0)
green=(0,255,0)
bright_green=(0,200,0)
blue=(0,0,255)

car_width=68
car_height=68

gameDisplay=pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("Race")

clock=pygame.time.Clock()

carImg=pygame.image.load('red.jpeg')

def thing_dodged(count):
	font=pygame.font.SysFont(None,25)
	text=font.render("Score: "+str(count),True,black)
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


def car(x,y):
	gameDisplay.blit(carImg,(x,y))
def text_object(text,font):
	textSurface=font.render(text,True,blue)
	return textSurface,textSurface.get_rect()

def disp_message(text):
	largeText=pygame.font.Font("freesansbold.ttf",60)
	TextSurf,TextRect=text_object(text,largeText)
	TextRect.center=((disp_width/2),(disp_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()
def crash():
	disp_message("You crashed..!!!")

def button(msg,x,y,w,h,inact_col,act_col):
	mouse=pygame.mouse.get_pos()
	if((x+w>mouse[0]>x) and (y+h>mouse[1]>y)):
		pygame.draw.rect(gameDisplay,act_col,(x,y,w,h))
	else:
		pygame.draw.rect(gameDisplay,inact_col,(x,y,w,h))

	smallText=pygame.font.Font("freesansbold.ttf",20)
	textSurf,textRect=text_object(msg,smallText)
	textRect.center=((x+(w/2)),(y+(h/2)))
	gameDisplay.blit(textSurf,textRect)


def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText=pygame.font.Font("freesansbold.ttf",80)
		TextSurf,TextRect=text_object("Race",largeText)
		TextRect.center=((disp_width/2),(disp_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		button("GO!",150,450,100,50,bright_green,green)
		button("QUIT !",550,450,100,50,red,bright_red)
		
		
		pygame.display.update()
		clock.tick(15)


def game_loop():

	x=disp_width*0.45
	y=disp_height*0.8

	x_change=0

	thing_startx=random.randrange(0,disp_width)
	thing_starty=-600
	thing_width=100
	thing_height=100
	thing_speed=5
	dodged=0

	game_exit=False


	while not game_exit:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x_change=-5
				elif event.key==pygame.K_RIGHT:
					x_change=5
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					x_change=0

		x+=x_change	
	
		gameDisplay.fill(white)
			
		things(thing_startx,thing_starty,thing_width,thing_height,black)
		
		thing_starty+=thing_speed

		car(x,y)
		thing_dodged(dodged)
		
		if x<0 or x>disp_width-car_width:
			crash()
		
		if thing_starty>disp_height:
			thing_starty=0-thing_height	
			thing_startx=random.randrange(0,disp_width)		
			dodged+=1
		if y < thing_starty + thing_height and thing_starty<y+car_height:
			if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
				crash()
		
		pygame.display.update()
	
		clock.tick(50)

game_intro()

game_loop()

pygame.quit()
quit()
