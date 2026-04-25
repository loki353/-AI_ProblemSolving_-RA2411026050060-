import tkinter as tk
from tkinter import messagebox
from logic import TicTacToeLogic

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Tic-Tac-Toe AI")
        self.root.geometry("450x650")
        self.root.configure(bg="#2c3e50")
        
        self.logic = TicTacToeLogic()
        self.use_alpha_beta = tk.BooleanVar(value=True)
        self.buttons = []
        self.game_over = False
        
        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="Tic-Tac-Toe AI", font=("Helvetica", 24, "bold"), 
                         bg="#2c3e50", fg="#ecf0f1", pady=20)
        header.pack()

        # Stats Panel
        self.stats_frame = tk.Frame(self.root, bg="#34495e", padx=10, pady=10, relief="raised", bd=1)
        self.stats_frame.pack(fill="x", padx=20)

        self.algo_label = tk.Label(self.stats_frame, text="Algorithm: Alpha-Beta Pruning", 
                                 font=("Helvetica", 10), bg="#34495e", fg="#bdc3c7")
        self.algo_label.pack()

        self.nodes_label = tk.Label(self.stats_frame, text="Nodes Explored: 0", 
                                  font=("Helvetica", 10), bg="#34495e", fg="#bdc3c7")
        self.nodes_label.pack()

        self.time_label = tk.Label(self.stats_frame, text="Execution Time: 0.00 ms", 
                                 font=("Helvetica", 10), bg="#34495e", fg="#bdc3c7")
        self.time_label.pack()

        # Grid Container
        grid_frame = tk.Frame(self.root, bg="#2c3e50", pady=20)
        grid_frame.pack()

        for i in range(9):
            btn = tk.Button(grid_frame, text="", font=("Helvetica", 20, "bold"), width=5, height=2,
                           bg="#ecf0f1", fg="#2c3e50", relief="flat",
                           command=lambda idx=i: self.player_move(idx))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Controls
        controls = tk.Frame(self.root, bg="#2c3e50", pady=10)
        controls.pack()

        self.toggle_btn = tk.Checkbutton(controls, text="Use Alpha-Beta Pruning", 
                                       variable=self.use_alpha_beta, onvalue=True, offvalue=False,
                                       bg="#2c3e50", fg="#ecf0f1", selectcolor="#34495e",
                                       command=self.update_algo_name)
        self.toggle_btn.pack()

        restart_btn = tk.Button(controls, text="Restart Game", font=("Helvetica", 12, "bold"),
                               bg="#e74c3c", fg="white", width=15, pady=5, relief="flat",
                               command=self.restart_game)
        restart_btn.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Your Turn (X)", font=("Helvetica", 14),
                                   bg="#2c3e50", fg="#f1c40f")
        self.status_label.pack(pady=10)

    def update_algo_name(self):
        name = "Alpha-Beta Pruning" if self.use_alpha_beta.get() else "Standard Minimax"
        self.algo_label.config(text=f"Algorithm: {name}")

    def player_move(self, idx):
        if self.logic.board[idx] == "" and not self.game_over:
            self.make_move(idx, self.logic.human_player)
            if not self.game_over:
                self.root.after(500, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return
        
        self.status_label.config(text="AI Thinking...")
        self.root.update()
        
        move, nodes, time_ms = self.logic.get_best_move(self.use_alpha_beta.get())
        
        if move != -1:
            self.make_move(move, self.logic.ai_player)
            self.nodes_label.config(text=f"Nodes Explored: {nodes}")
            self.time_label.config(text=f"Execution Time: {time_ms:.2f} ms")
            
            if not self.game_over:
                self.status_label.config(text="Your Turn (X)")

    def make_move(self, idx, player):
        self.logic.board[idx] = player
        color = "#3498db" if player == "X" else "#e67e22"
        self.buttons[idx].config(text=player, state="disabled", disabledforeground=color)
        
        winner, combo = self.logic.check_winner(self.logic.board)
        if winner:
            self.end_game(winner, combo)

    def end_game(self, winner, combo):
        self.game_over = True
        if winner == "Draw":
            self.status_label.config(text="Game Draw!", fg="#95a5a6")
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            self.status_label.config(text=f"Winner: {winner}!", fg="#2ecc71")
            # Highlight winning cells
            for idx in combo:
                self.buttons[idx].config(bg="#2ecc71", disabledforeground="white")
            messagebox.showinfo("Game Over", f"Player {winner} has won the game!")

    def restart_game(self):
        self.logic = TicTacToeLogic()
        self.game_over = False
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#ecf0f1")
        self.status_label.config(text="Your Turn (X)", fg="#f1c40f")
        self.nodes_label.config(text="Nodes Explored: 0")
        self.time_label.config(text="Execution Time: 0.00 ms")
        self.update_algo_name()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
