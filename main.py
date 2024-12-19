import pygame
import sys
pygame.init()

screen_width = 900
screen_height = 1700
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Jeopardy')

BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0) 

font = pygame.font.Font(None, 100)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLUE)
    text = font.render('Jeopardy', True, YELLOW)
    text_rect = text.get_rect(center=(830, 200))
    screen.blit(text, text_rect)

    text2 = font.render('Play Game', True, YELLOW)
    text_rect2 = text.get_rect(center=(830, 500))
    screen.blit(text2, text_rect2)
    pygame.display.flip()
    count = 0

