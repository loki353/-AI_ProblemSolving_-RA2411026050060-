import time
import copy

class TicTacToeLogic:
    def __init__(self):
        # Initialize board as a list of 9 empty strings
        self.board = [""] * 9
        self.human_player = "X"
        self.ai_player = "O"
        self.nodes_explored = 0

    def check_winner(self, board):
        """Checks for a winner and returns 'X', 'O', 'Draw', or None."""
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for combo in win_conditions:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                return board[combo[0]], combo
        
        if "" not in board:
            return "Draw", None
        
        return None, None

    def get_available_moves(self, board):
        return [i for i, spot in enumerate(board) if spot == ""]

    def minimax(self, board, depth, is_maximizing):
        """Standard Minimax algorithm."""
        self.nodes_explored += 1
        
        winner, _ = self.check_winner(board)
        if winner == self.ai_player:
            return 10 - depth
        if winner == self.human_player:
            return depth - 10
        if winner == "Draw":
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.ai_player
                score = self.minimax(board, depth + 1, False)
                board[move] = ""
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.human_player
                score = self.minimax(board, depth + 1, True)
                board[move] = ""
                best_score = min(score, best_score)
            return best_score

    def alpha_beta(self, board, depth, alpha, beta, is_maximizing):
        """Minimax with Alpha-Beta Pruning."""
        self.nodes_explored += 1
        
        winner, _ = self.check_winner(board)
        if winner == self.ai_player:
            return 10 - depth
        if winner == self.human_player:
            return depth - 10
        if winner == "Draw":
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.ai_player
                score = self.alpha_beta(board, depth + 1, alpha, beta, False)
                board[move] = ""
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cut-off
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.human_player
                score = self.alpha_beta(board, depth + 1, alpha, beta, True)
                board[move] = ""
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cut-off
            return best_score

    def get_best_move(self, use_alpha_beta=True):
        """Calculates best move using chosen algorithm and returns results."""
        self.nodes_explored = 0
        start_time = time.perf_counter()
        
        best_score = -float('inf')
        move_to_make = -1
        
        available_moves = self.get_available_moves(self.board)
        
        # If board is empty, picking a corner or center is fast and good
        # But we let the algorithm calculate for demo purposes if it's not too slow
        
        for move in available_moves:
            self.board[move] = self.ai_player
            if use_alpha_beta:
                score = self.alpha_beta(self.board, 0, -float('inf'), float('inf'), False)
            else:
                score = self.minimax(self.board, 0, False)
            self.board[move] = ""
            
            if score > best_score:
                best_score = score
                move_to_make = move
        
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000 # convert to ms
        
        return move_to_make, self.nodes_explored, execution_time
