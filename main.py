from gui import GuessTheNumberGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = GuessTheNumberGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
