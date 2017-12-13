import pygame
import time

pygame.init()

pygame.font.get_fonts()

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('testing game')

pygame.display.update

gameExit = False

clock = pygame.time.Clock()

font = pygame.font.SysFont('mingliupmingliumingliuhkscs',50)

def message_to_screen(color,x,y):
	screen_text = font.render('中文',True,color)
	gameDisplay.blit(screen_text,[x,y])
	
def show_text():
	gameDisplay.fill(white)
	message_to_screen(red,400,300)
	pygame.display.update()
	#pygame.display.update()
	
def show_text_2():
	message_to_screen(black,100,100)
	pygame.display.update()
	
def original_board():
	gameDisplay.fill(white)
	pygame.display.update()


x = 0

gameDisplay.fill(white)
pygame.display.update()

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				x += 1
			if event.key == pygame.K_a:
				x -= 1
				if x < 0:
					x = 0
			
	if x == 0:
		original_board()
	elif x == 1:
		show_text()
	elif x == 2:
		show_text_2()
				#break

	#clock.tick()
pygame.quit()
quit()