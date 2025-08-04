import tkinter as tk
from tkinter import messagebox

# Game Logic
def start_game():
    label.config(text="You're at a crossroad. Where do you want to go?")
    left_button.config(text="Go Left", command=go_left)
    right_button.config(text="Go Right", command=game_over_hole)
    left_button.pack(pady=10)
    right_button.pack(pady=10)

def go_left():
    label.config(text="You come to a lake. Do you wait for a boat or swim across?")
    left_button.config(text="Wait", command=wait_for_boat)
    right_button.config(text="Swim", command=game_over_crocodile)

def wait_for_boat():
    label.config(text="You arrive at an island with 3 doors: red, yellow, and blue. Choose one.")
    left_button.config(text="Red", command=game_over_fire)
    middle_button.config(text="Yellow", command=win_game)
    right_button.config(text="Blue", command=game_over_beasts)
    middle_button.pack(pady=10)

def game_over_hole():
    messagebox.showinfo("Game Over", "😈 You fell into a hole. Game over.")
    root.quit()

def game_over_crocodile():
    messagebox.showinfo("Game Over", "🐊 You got attacked by a crocodile. Game over.")
    root.quit()

def game_over_fire():
    messagebox.showinfo("Game Over", "🔥 It's a room full of fire. Game over.")
    root.quit()

def game_over_beasts():
    messagebox.showinfo("Game Over", "🐻 You enter a room of beasts. Game over.")
    root.quit()

def win_game():
    messagebox.showinfo("Victory!", "🎉 You found the treasure! You win!")
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("🏝️ Treasure Island Game")
root.geometry("500x300")

label = tk.Label(root, text="Welcome to Treasure Island!\nYour mission is to find the treasure. 🏴‍☠️", font=("Arial", 12), wraplength=400, justify="center")
label.pack(pady=20)

left_button = tk.Button(root, text="", width=20, height=2)
middle_button = tk.Button(root, text="", width=20, height=2)
right_button = tk.Button(root, text="", width=20, height=2)

start_game()

root.mainloop()
