import pygame
import sys
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trivia Game - Streak Mode")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 50)

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

questions = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    Question("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
    Question("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Hemingway", "Austen"], "Shakespeare"),
    Question("What is the largest planet?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter"),
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
    game_over = False

    while True:
        current_question = 0
        streak = 0

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
                        streak += 1
                        current_question += 1
                        if current_question >= len(questions):
                            game_over = True  # Player answered all questions correctly
                    else:
                        game_over = True  # Player got an answer wrong
                    break

            # Display Streak
            streak_text = font.render(f"Streak: {streak}", True, BLACK)
            screen.blit(streak_text, (50, screen_height - 50))
            
            pygame.display.flip()

        # Game over screen with streak
        screen.fill(WHITE)
        game_over_text = large_font.render("Game Over!", True, BLACK)
        streak_end_text = font.render(f"Your Streak: {streak}", True, BLACK)
        
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
        screen.blit(streak_end_text, (screen_width // 2 - streak_end_text.get_width() // 2, screen_height // 2))
        
        # Play Again button
        play_again_button = Button(100, screen_height // 1.5, 600, 50, GREEN, "Play Again")
        play_again_button.draw(screen)

        pygame.display.flip()

        # Wait for the player to either quit or click "Play Again"
        play_again = False
        while not play_again:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.is_clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                        play_again = True
                        game_over = False

