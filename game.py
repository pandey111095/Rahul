import pygame 
import time
import random

pygame.init()

disp_width=800
disp_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

car_width=68

gameDisplay=pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("Race")

clock=pygame.time.Clock()

carImg=pygame.image.load('red.jpeg')

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


def car(x,y):
	gameDisplay.blit(carImg,(x,y))
def text_object(text,font):
	textSurface=font.render(text,True,red)
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

def game_loop():

	x=disp_width*0.45
	y=disp_height*0.8

	x_change=0

	thing_startx=random.randrange(0,disp_width)
	thing_starty=-600
	thing_width=100
	thing_height=100
	thing_speed=5

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
		
		if x<0 or x>disp_width-car_width:
			crash()
		
		if thing_starty>disp_height:
			thing_starty=0-thing_height	
			thing_startx=random.randrange(0,disp_width)		
		
		pygame.display.update()
	
		clock.tick(50)

game_loop()

pygame.quit()
quit()

