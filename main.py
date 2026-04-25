"""
Tic-Tac-Toe AI Game - Main Entry Point
Created for AI Assignment Comparison: Minimax vs Alpha-Beta Pruning
"""

import tkinter as tk
from gui import TicTacToeGUI

def main():
    root = tk.Tk()
    # Provide a simple custom icon if desired, otherwise default
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
