import pygame
import sys
import tkinter as tk
from tkinter import messagebox
pygame.init()
questions = [
    {"question": "", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"], "answer": "Shakespeare"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "Which element has the chemical symbol 'Ar'?", "options": ["Argon", "Iron", "Nitrogen", "Aluminum"], "answer": "Oxygen"},
    {"question": "What is 30 x 896", "options": ["26880", "26480", "26870", "25880"], "answer": "26880"},
]

screen_width = 900
screen_height = 1700
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Trivia')

Black = (0, 0, 0) 
White = (255, 255, 255) 

font = pygame.font.Font(None, 100)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(White)
    text = font.render('Trivia', True, Black)
    text_rect = text.get_rect(center=(830, 200))
    screen.blit(text, text_rect)

    text2 = font.render('Play Game', True, Black)
    text_rect2 = text.get_rect(center=(750, 500))
    screen.blit(text2, text_rect2)
    pygame.display.flip()
    count = 0

def check_answer(selected_answer):
    global current_question, score
    if selected_answer == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        show_score()
        answer_buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=20, height=2, command=lambda i=i: check_answer(answer_buttons[i]['text']))
    button.pack(pady=5)
    answer_buttons.append(button)