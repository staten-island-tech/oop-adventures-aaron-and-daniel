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
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
]