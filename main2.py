import pygame
import sys
import random  # Import random to shuffle questions and answers
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
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

questions = [
<<<<<<< HEAD:main2.py
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris", ["Berlin", "Madrid", "Rome"]),
    Question("What is 5 + 7?", ["10", "11", "12", "13"], "12", ["10", "11", "13"]),
    Question("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Hemingway", "Austen"], "Shakespeare", ["Dickens", "Hemingway", "Austen"]),
    Question("What is the largest planet?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter", ["Earth", "Mars", "Venus"]),
    Question("Who is the 35th president of the United States?", ["Dwight David Eisenhower", "Lyndon Johnson", "John Fitzgerald Kennedy", "James Earl Carter Jr."], "John Fitzgerald Kennedy",["Dwight David Eisenhower", "Lyndon Johnson", "James Earl Carter Jr."]),
    Question("Who wrote the Harry Potter Series?", ["Shakespeare", "Dickens", "JK Rowling", "Austen"], "JK Rowling",["Shakespeare", "Dickens","Austen"]),
    Question("Which element has the chemical symbol 'Ar'?", ["Argon", "Iron", "Nitrogen", "Aluminum"], "Argon",["Iron", "Nitrogen", "Aluminum"]),
    Question("What is 30 x 896", ["26880", "26480", "26870", "25880"], "26880",["26480", "26870", "25880"]),
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris", ["Berlin", "Madrid", "Rome"]),
=======
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    Question("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
    Question("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Hemingway", "Austen"], "Shakespeare"),
    Question("What is the largest planet?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter"),
>>>>>>> main:main.py
]

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, screen, color=None):
        if color:
            pygame.draw.rect(screen, color, self.rect)
        else:
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
    def reset_game():
        # Resets the game variables
        nonlocal current_question, score, streak, highest_streak, game_over
        current_question = 0
        score = 0
        streak = 0
        highest_streak = 0
        game_over = False
        random.shuffle(questions)
        for question in questions:
            random.shuffle(question.options)

    current_question = 0
    score = 0
    streak = 0
    highest_streak = 0
    game_over = False
    
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.options)
    
    while True:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            # Display game over screen with Play Again button
            game_over_text = large_font.render("Game Over!", True, BLACK)
            score_text = font.render(f"Your Score: {score}/{len(questions)}", True, BLACK)
            streak_text = font.render(f"Current Streak: {streak}", True, BLACK)
            highest_streak_text = font.render(f"Highest Streak: {highest_streak}", True, BLACK)

            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
            screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
            screen.blit(streak_text, (20, 20))  # Display current streak at top-left corner
            screen.blit(highest_streak_text, (screen_width - highest_streak_text.get_width() - 20, 20))  # Display highest streak at top-right corner
            
            # Draw the Play Again button
            play_again_button = Button(screen_width // 2 - 100, screen_height // 1.5, 200, 50, BLUE, "Play Again")
            play_again_button.draw(screen)

            pygame.display.flip()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_again_button.is_clicked(mouse_pos, mouse_pressed):
                reset_game()  # Reset the game variables to start a new game

        else:
            # Regular trivia game flow
            question = questions[current_question]
            question_text = font.render(question.question, True, BLACK)
            screen.blit(question_text, (50, 50))

            buttons = []
            for i, option in enumerate(question.options):
                button = Button(100, 150 + i * 60, 600, 50, BLUE, option)
                buttons.append(button)
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            selected_wrong = False
            selected_correct = False
            selected_answer = ""

            for button in buttons:
                if button.is_clicked(mouse_pos, mouse_pressed):
                    selected_answer = button.text
                    if button.text == question.correct_answer:
                        score += 1
                        selected_correct = True
                        streak += 1  # Increase streak for correct answer
                        if streak > highest_streak:  # Update highest streak if necessary
                            highest_streak = streak
                    else:
                        selected_wrong = True
                        streak = 0  # Reset streak on wrong answer

            for button in buttons:
                if selected_answer == button.text:
                    if selected_correct:
                        button.draw(screen, GREEN)
                    elif selected_wrong:
                        button.draw(screen, RED)
                    else:
                        button.draw(screen)
                else:
                    button.draw(screen)

            if selected_wrong:
                game_over = True

            if selected_correct and not selected_wrong:
                pygame.time.wait(1000)  # Wait for 1 second to show the correct answer
                current_question += 1
                if current_question >= len(questions):
                    game_over = True

            pygame.display.flip()

    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  
                pygame.quit()
                sys.exit()
run_trivia_game()
