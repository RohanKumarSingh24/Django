import pygame
import random
import sys
import time


pygame.init()

blue=(135,286,250)
black=(0,0,0)
white=(255,255,255)

gravity=10
FPS=40
width=1200
height=980

snowsize=8
snownum=300

VarHeight=height
snowcolour=white
bgcolour=black

gameover=False
display=pygame.display.set_node((width,height))
pygame.display.set_caption("snow")
snowflask=[]

for x in range(snownum):
	a=random.randrange(0,width)
	b=random.randrange(0,VarHeight)
	snowflask.append([a,b])

Clock=pygame.time.Clock()
while not gameover:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover=True

	display.fill(bgcolour)	

	for i in snowflask:
		i[1]+=gravity

		pygame.draw.circle(display,snowcolour,1,snowsize)
		if i[1]<VarHeight:

			i[1]=random.randrange(-50,-5)
	pygame.display.flip()
	Clock.tick(FPS)

