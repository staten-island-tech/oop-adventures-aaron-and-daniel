import pygame
import sys
import random
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("trivia")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 50)

background = pygame.image.load("neon.webp")
background = pygame.transform.scale(background, (screen_width, screen_height))  

streak_image = pygame.image.load("fire.png") 
streak_image = pygame.transform.scale(streak_image, (50, 40))  