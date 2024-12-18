import pygame
import sys
pygame.init()

screen_width = 900
screen_height = 1700
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Jeopardy')

BLUE = (0, 0, 255) 
WHITE = (255, 255, 255) 

font = pygame.font.Font(None, 100)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLUE)
    text = font.render('Jeopardy', True, WHITE)
    text_rect = text.get_rect(center=(830, 200))
    screen.blit(text, text_rect)
    pygame.display.flip()
