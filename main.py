import pygame
import sys
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

class Question:
    def __init__(self, question, options, correct_answer, wrong_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.wrong_answer = wrong_answer

questions = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris", ["Berlin", "Madrid", "Rome"]),
    Question("What is 5 + 7?", ["10", "11", "12", "13"], "12", ["10", "11", "13"]),
    Question("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Hemingway", "Austen"], "Shakespeare", ["Dickens", "Hemingway", "Austen"]),
    Question("What is the largest planet?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter", ["Earth", "Mars", "Venus"]),
]

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0]: 
                return True
        return False

def run_trivia_game():
    current_question = 0
    score = 0
    game_over = False
    
    while not game_over:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        question = questions[current_question]
        question_text = font.render(question.question, True, BLACK)
        screen.blit(question_text, (50, 50))
        
        buttons = []
        for i, option in enumerate(question.options):
            button = Button(100, 150 + i * 60, 600, 50, BLUE, option)
            button.draw(screen)
            buttons.append(button)
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        for button in buttons:
            if button.is_clicked(mouse_pos, mouse_pressed):
                if button.text == question.correct_answer:
                    score += 1
                    current_question += 1
            if button.is_clicked(mouse_pos, mouse_pressed):    
                if button.text == question.wrong_answer:
                    score += 0
                    current_question += 0 
                
                if current_question >= len(questions):
                    game_over = True
                break
        pygame.display.flip()
    screen.fill(WHITE)
    game_over_text = large_font.render("Game Over!", True, BLACK)
    score_text = font.render(f"Your Score: {score}/{len(questions)}", True, BLACK)
    
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
    
    pygame.display.flip()
run_trivia_game()
