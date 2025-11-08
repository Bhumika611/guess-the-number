import random

class GameLogic:
    """Handles the logic for Guess The Number game."""

    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self, guess: int) -> str:
        """Check the user's guess and return feedback."""
        self.attempts += 1

        if guess < 1 or guess > 100:
            return "🚫 Number must be between 1 and 100!"
        elif guess < self.secret_number:
            return "Too low! Try a higher number. 🔼"
        elif guess > self.secret_number:
            return "Too high! Try a lower number. 🔽"
        else:
            return f"🎉 Correct! You guessed it in {self.attempts} attempts!"

    def reset_game(self):
        """Reset the game with a new number."""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
