import pygame
import sys
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trivia Game")

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
            if mouse_pressed[0]:  # Left mouse button
                return True
        return False

# Game loop
def run_trivia_game():
    current_question = 0
    score = 0
    game_over = False
    
    # Game loop
    while not game_over:
        screen.fill(WHITE)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display the current question
        question = questions[current_question]
        question_text = font.render(question.question, True, BLACK)
        screen.blit(question_text, (50, 50))
        
        # Create buttons for the answer options
        buttons = []
        for i, option in enumerate(question.options):
            button = Button(100, 150 + i * 60, 600, 50, BLUE, option)
            button.draw(screen)
            buttons.append(button)
        
        # Check if any button is clicked
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        for button in buttons:
            if button.is_clicked(mouse_pos, mouse_pressed):
                if button.text == question.correct_answer:
                    score += 1
                current_question += 1
                
                if current_question >= len(questions):
                    game_over = True
                break
        
        # Update the screen
        pygame.display.flip()
    
    # Display Game Over screen and score
    screen.fill(WHITE)
    game_over_text = large_font.render("Game Over!", True, BLACK)
    score_text = font.render(f"Your Score: {score}/{len(questions)}", True, BLACK)
    
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
    
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait 3 seconds before closing
    pygame.quit()
    sys.exit()

# Run the trivia game
run_trivia_game()






