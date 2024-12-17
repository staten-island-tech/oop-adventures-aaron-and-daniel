import pygame
import sys
pygame.init()
screen_width = 1700
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
text_font = pygame.font.SysFont("Arial", 30)
def draw_text(text, font,text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
run = True
while run:
    screen.fill((0, 0, 255))
    draw_text("Jeopardy", text_font, (0, 0, 0), 220, 150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()