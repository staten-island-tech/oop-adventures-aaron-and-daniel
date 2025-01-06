import tkinter as tk
def on_button_click():
    print("Game Starting")

root = tk.Tk()
root.title("Clickable Button Example")
button = tk.Button(root, text="Play Game", command=on_button_click)
button.pack(pady=20)
