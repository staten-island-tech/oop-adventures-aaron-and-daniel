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
    Question("Which country has the Eiffel Tower?", ["Germany", "Spain", "France", "Italy"], "France"),
    Question("What is the currency used in Japan?", ["Yuan", "Won", "Yen", "Ringgit"], "Yen"),
    Question("Which animal is the King of the Jungle?", ["Lion", "Tiger", "Elephant", "Bear"], "Lion")
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