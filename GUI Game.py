import tkinter as tk
from tkinter import messagebox
from functools import partial
import random

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic-Tac-Toe")
        self.geometry("250x325")

        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]

        self.player = "X"
        self.ai_player = "O"
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, width=5, height=2, command=partial(self.handle_turn, row=i, col=j))
                button.grid(row=i, column=j)

    def handle_turn(self, row, col):
        button = self.grid_slaves(row=row, column=col)[0]
        button.config(text=self.player, state="disable")
        self.board[row*3 + col] = self.player

        if self.check_game_over():
            self.game_over()
        else:
            self.ai_turn()

    def ai_turn(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

        move = self.minimax(self.board, self.player)
        row, col = move // 3, move % 3
        button = self.grid_slaves(row=row, column=col)[0]
        button.config(text=self.player, state="disable")
        self.board[row*3 + col] = self.player
        if self.check_game_over():
            self.game_over()
        else:
            self.player = "X"

    def check_game_over(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] and self.board[i] != "-":
                return True
        # check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] and self.board[i] != "-":
                return True
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            return True
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-":
            return True
        # check for tie
        if "-" not in self.board:
            return True
        return False

    def game_over(self):
        for button in self.grid_slaves():
            button.config(state="disable")

        if "-" not in self.board:
            messagebox.showinfo("Tie!", "It's a tie!")
        elif self.player == self.ai_player:
            messagebox.showinfo("Winner!", f"{self.ai_player} wins!")
        else:
            messagebox.showinfo("Winner!", f"{self.player} wins!")

    def minimax(self, board, player):
        if self.check_game_over():
            return 0

        if self.check_game_over():
            if player == self.ai_player:
                return 1
            else:
                return -1

        scores = []
        moves = []

        for i, square in enumerate(board):
            if square == "-":
                new_board = board[:]
                new_board[i] = player
                if self.check_game_over():
                    scores.append(0)
                    moves.append(i)
                    continue
                if player == self.ai_player:
                    score = self.minimax(new_board, "X")
                else:
                    score = self.minimax(new_board, "O")
                scores.append(score)
                moves.append(i)

        if scores == []:
            return 0

        if player == self.ai_player:
            best_score_index = scores.index(max(scores))
        else:
            best_score_index = scores.index(min(scores))

        return moves[best_score_index]

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
