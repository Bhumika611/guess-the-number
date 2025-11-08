import tkinter as tk
from tkinter import messagebox
from game_logic import GameLogic

class GuessTheNumberGUI:
    """Graphical interface for the Guess The Number game."""

    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess The Number Game")
        self.root.geometry("420x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#fde2f2")

        # Initialize logic
        self.logic = GameLogic()

        # Heading
        tk.Label(
            root,
            text="Welcome to the Guessing Game!",
            font=("Segoe UI", 16, "bold"),
            bg="#fa14f2",
            fg="#0f708e"
        ).pack(pady=20)

        tk.Label(
            root,
            text="I’ve picked a number between 1 and 100.\nCan you guess it?",
            font=("Segoe UI", 12),
            bg="#fee8f7"
        ).pack(pady=10)

        # Entry field
        self.entry = tk.Entry(root, font=("Segoe UI", 12), justify="center", width=10)
        self.entry.pack(pady=5)

        # Buttons
        self.guess_button = tk.Button(
            root, text="Submit Guess", font=("Segoe UI", 11, "bold"),
            bg="#34a853", fg="white", width=15, command=self.submit_guess
        )
        self.guess_button.pack(pady=15)

        self.feedback_label = tk.Label(
            root, text="", font=("Segoe UI", 12), bg="#e8f0fe", fg="#202124"
        )
        self.feedback_label.pack(pady=10)

        self.reset_button = tk.Button(
            root, text="Play Again", font=("Segoe UI", 10, "bold"),
            bg="#fbbc04", fg="black", width=12, command=self.reset_game
        )
        self.reset_button.pack(pady=10)
        self.reset_button.config(state=tk.DISABLED)

        tk.Label(
            root,
            text="Developed by Bhumika Macharla | SkillCraft Internship",
            font=("Segoe UI", 9),
            bg="#fce2f8",
            fg="#5f6368"
        ).pack(side="bottom", pady=10)

    def submit_guess(self):
        """Handle the guess submission."""
        user_input = self.entry.get()

        if not user_input.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number between 1 and 100.")
            return

        guess = int(user_input)
        result = self.logic.check_guess(guess)
        self.feedback_label.config(text=result)

        if "Correct" in result:
            self.guess_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            messagebox.showinfo("Congratulations!", f"You found the number {self.logic.secret_number}!")

    def reset_game(self):
        """Restart the game."""
        self.logic.reset_game()
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
