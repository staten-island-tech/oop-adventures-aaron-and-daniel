import pygame
import sys
import random
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trivia")

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
    Question("Who is the 35th president of the United States?", ["Dwight David Eisenhower", "Lyndon Johnson", "John Fitzgerald Kennedy", "James Earl Carter Jr."], "John Fitzgerald Kennedy"),
    Question("Who wrote the Harry Potter Series?", ["Shakespeare", "Dickens", "JK Rowling", "Austen"], "JK Rowling"),
    Question("Which element has the chemical symbol 'Ar'?", ["Argon", "Iron", "Nitrogen", "Aluminum"], "Argon"),
    Question("What is 30 x 896", ["26880", "26480", "26870", "25880"], "26880"),
    Question("Which famous play features a character named Romeo?", ["Swan's Lake", "Nutcracker", "Hamlet", "Romeo and Juilet"], "Romeo and Juilet"),
    Question("Who invented the lightbulb?", ["Nikola Tesla", "Benjamin Franklin", "Marie Curie", "Thomas Edison"], "Thomas Edison"),
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



def reset_game():
    global current_question, score, streak, highest_streak, game_over
    current_question = 0
    score = 0
    streak = 0
    highest_streak = 0
    game_over = False
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.options)



def draw_game_over_screen():
    game_over_text = large_font.render("Game Over!", True, BLACK)
    score_text = font.render(f"Your Score: {score}/{len(questions)}", True, BLACK)
    streak_text = font.render(f"Current Streak: {streak}", True, BLACK)
    highest_streak_text = font.render(f"Highest Streak: {highest_streak}", True, BLACK)

    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
    screen.blit(streak_text, (20, 20))
    screen.blit(highest_streak_text, (screen_width - highest_streak_text.get_width() - 20, 20))

    play_again_button = Button(screen_width // 2 - 100, screen_height // 1.5, 200, 50, BLUE, "Play Again")
    play_again_button.draw(screen)

    return play_again_button



def handle_button_click(buttons, mouse_pos, mouse_pressed, question):
    selected_answer = ""
    selected_correct = False
    selected_wrong = False

    for button in buttons:
        if button.is_clicked(mouse_pos, mouse_pressed):
            selected_answer = button.text
            if selected_answer == question.correct_answer:
                selected_correct = True
            else:
                selected_wrong = True

    return selected_answer, selected_correct, selected_wrong



def update_score_and_streak(selected_correct, selected_wrong):
    global score, streak, highest_streak
    if selected_correct:
        score += 1
        streak += 1
        if streak > highest_streak:
            highest_streak = streak
    elif selected_wrong:
        streak = 0



def draw_buttons(buttons, selected_answer, selected_correct, selected_wrong):
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



def check_game_over(selected_wrong, selected_correct):
    global game_over, current_question
    if selected_wrong:
        game_over = True

    if selected_correct and not selected_wrong:
        pygame.time.wait(1000)
        current_question += 1
        if current_question >= len(questions):
            game_over = True



def run_trivia_game():
    global current_question, score, streak, highest_streak, game_over
    reset_game()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            play_again_button = draw_game_over_screen()
            if play_again_button.is_clicked(mouse_pos, mouse_pressed):
                reset_game()

        else:
            question = questions[current_question]
            question_text = font.render(question.question, True, BLACK)
            screen.blit(question_text, (50, 50))

            buttons = []
            for i, option in enumerate(question.options):
                button = Button(100, 150 + i * 60, 600, 50, BLUE, option)
                buttons.append(button)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            selected_answer, selected_correct, selected_wrong = handle_button_click(buttons, mouse_pos, mouse_pressed, question)
            update_score_and_streak(selected_correct, selected_wrong)
            draw_buttons(buttons, selected_answer, selected_correct, selected_wrong)
            check_game_over(selected_wrong, selected_correct)

        pygame.display.flip()


run_trivia_game()