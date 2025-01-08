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

# Load the streak image
streak_image = pygame.image.load("fire.png") 
streak_image = pygame.transform.scale(streak_image, (50, 40))  

def load_highest_streak():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def save_highest_streak(streak):
    with open("highscore.txt", "w") as file:
        file.write(str(streak))

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

questions = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    Question("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
    Question("Who was the first president of the US?", ["Donald Trump", "George Washington", "John Adams", "Abraham Lincoln"], "George Washington"),
    Question("What is the largest planet?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter"),
    Question("What is the biggest state in the US?", ["Texas", "New York", "Alaska", "California"], "Alaska"),
    Question("What is the biggest building in the world?", ["Freedom Tower", "Burj Khalifa", "Empire State Building", "Leaning Tower of Pisa"], "Burj Khalifa"),
    Question("What is the biggest basketball league?", ["NBL", "KBL", "NBA", "Euro-League"], "NBA"),
    Question("Which is the largest ocean on Earth?", ["Atlantic", "Pacific", "Indian", "Arctic"], "Pacific"),
    Question("In which year did World War II end?", ["1940", "1942", "1945", "1950"], "1945"),
    Question("What is the smallest country in the world?", ["Vatican City", "Monaco", "San Marino", "Liechtenstein"], "Vatican City"),  
    Question("Which country is famous for the Eiffel Tower?", ["Germany", "Spain", "France", "Italy"], "France"),
    Question("What is the currency used in Japan?", ["Yuan", "Won", "Yen", "Ringgit"], "Yen"),
    Question("Which animal is known as the King of the Jungle?", ["Lion", "Tiger", "Elephant", "Bear"], "Lion")
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
        nonlocal current_question, score, streak, highest_streak, game_over, power_up_used
        current_question = 0
        score = 0
        streak = 0
        power_up_used = False
        game_over = False
        random.shuffle(questions)
        for question in questions:
            random.shuffle(question.options)

    current_question = 0
    score = 0
    streak = 0
    power_up_used = False
    highest_streak = load_highest_streak()  
    game_over = False
    
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.options)
    
    while True:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            game_over_text = large_font.render("Game Over!", True, WHITE)
            score_text = font.render(f"Your Score: {score}/{len(questions)}", True, WHITE)
            streak_text = font.render(f"Current Streak: {streak}", True, WHITE)
            highest_streak_text = font.render(f"Highest Streak: {highest_streak}", True, WHITE)

            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
            screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
            screen.blit(streak_text, (20, 20)) 
            screen.blit(highest_streak_text, (screen_width - highest_streak_text.get_width() - 20, 20))  
            
            play_again_button = Button(screen_width // 2 - 100, screen_height // 1.5, 200, 50, BLUE, "Play Again")
            play_again_button.draw(screen)

            pygame.display.flip()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_again_button.is_clicked(mouse_pos, mouse_pressed):
                if streak > highest_streak:
                    highest_streak = streak
                    save_highest_streak(highest_streak)  
                reset_game()  

        else:
            question = questions[current_question]
            question_text = font.render(question.question, True, WHITE)
            screen.blit(question_text, (205, 100))

            # Power-Up Activation
            if streak >= 5 and not power_up_used:
                use_power_up_button = Button(screen_width // 2 - 100, screen_height // 1.5, 250, 50, BLUE, "Use 50/50 Powerup")
                use_power_up_button.draw(screen)

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if use_power_up_button.is_clicked(mouse_pos, mouse_pressed):
                    power_up_used = True
                    # Ensure correct answer stays and remove two random incorrect options
                    correct_option = question.correct_answer
                    incorrect_options = [option for option in question.options if option != correct_option]
                    random.shuffle(incorrect_options)
                    # Keep only the correct answer and one random incorrect answer
                    question.options = [correct_option] + incorrect_options[:1]

            # Display answer choices
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
                        streak += 1  
                        if streak > highest_streak:  
                            highest_streak = streak
                    else:
                        selected_wrong = True
                        streak = 0  

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
                pygame.time.wait(100)  
                current_question += 1
                if current_question >= len(questions):
                    game_over = True
            screen.blit(streak_image, (10, 10))  
            streak_text = font.render(f"Streak: {streak}", True, WHITE)
            screen.blit(streak_text, (60, 15)) 

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
