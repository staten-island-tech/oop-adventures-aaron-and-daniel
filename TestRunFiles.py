import tkinter as tk
from tkinter import messagebox

# List of questions and answers
questions = [
    {"question": "Who is the 35th president of the United States", "options": ["Dwight David Eisenhower", "Lyndon Johnson", "John Fitzgerald Kennedy", "James Earl Carter Jr."], "answer": "John Fitzgerald Kennedy"},
    {"question": "Who wrote the Harry Potter Series?", "options": ["Shakespeare", "Dickens", "JK Rowling", "Austen"], "answer": "JK Rowling"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "Which element has the chemical symbol 'Ar'?", "options": ["Argon", "Iron", "Nitrogen", "Aluminum"], "answer": "Argon"},
    {"question": "What is 30 x 896", "options": ["26880", "26480", "26870", "25880"], "answer": "26880"},
]

# Global variable to keep track of the current question and the score
current_question = 0
score = 0

# Function to check the answer and move to the next question
def check_answer(selected_answer):
    global current_question, score

    # Check if the answer is correct
    if selected_answer == questions[current_question]["answer"]:
        score += 1

    # Move to the next question
    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_score()

# Function to display the current question and options
def display_question():
    global current_question

    question_data = questions[current_question]
    question_label.config(text=question_data["question"])

    for i in range(4):
        answer_buttons[i].config(text=question_data["options"][i], state=tk.NORMAL)

# Function to show the score at the end
def show_score():
    global score
    messagebox.showinfo("Game Over", f"Your score is: {score}/{len(questions)}")
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Trivia Game")

# Create question label
question_label = tk.Label(root, text="", font=('Helvetica', 14), width=50, height=4)
question_label.pack(pady=20)

# Create answer buttons
answer_buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=20, height=2, command=lambda i=i: check_answer(answer_buttons[i]['text']))
    button.pack(pady=5)
    answer_buttons.append(button)

# Display the first question
display_question()

# Run the application
root.mainloop()
