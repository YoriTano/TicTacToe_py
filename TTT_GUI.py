import tkinter as tk
from tkinter import messagebox
from TicTacToe_finished import marker_choice, choose_first, has_won, board_isfull, replay 

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Set background color to teal
        self.root.configure(bg='#ADD8E6')

        self.buttons = {}
        for i in range(1, 10):
            self.buttons[i] = tk.Button(root, text=" ", font=('Arial', 24), width=6, height=3, command=lambda idx=i: self.on_click(idx))
            row = (i - 1) // 3
            col = (i - 1) % 3
            self.buttons[i].grid(row=row, column=col)

        self.the_board = [' '] * 10
        self.player1_marker, self.player2_marker = marker_choice()
        self.turn = choose_first()
        print(f"{self.turn} will go first!")

    def on_click(self, position):
        if self.the_board[position] == ' ':
            self.place_marker(position)
            self.update_button(position)
            if has_won(self.the_board, self.player1_marker if self.turn == "player 1" else self.player2_marker):
                winner = "Player 1" if self.turn == "player 1" else "Player 2"
                messagebox.showinfo("Winner!", f"{winner} wins!")
                self.reset_game()
            elif board_isfull(self.the_board):
                messagebox.showinfo("Tie Game", "It's a tie!")
                self.reset_game()
            else:
                self.switch_turn()

    def place_marker(self, position):
        self.the_board[position] = self.player1_marker if self.turn == "player 1" else self.player2_marker

    def update_button(self, position):
        marker_text = "❌" if self.the_board[position] == self.player1_marker else "🔵"
        marker_color = 'blue' if marker_text == '❌' else 'red'
        self.buttons[position].config(text=marker_text, fg=marker_color)

    def switch_turn(self):
        self.turn = "player 2" if self.turn == "player 1" else "player 1"

    def reset_game(self):
        if replay():
            self.the_board = [' '] * 10
            self.turn = choose_first()
            print(f"{self.turn} will go first!")
            for i in range(1, 10):
                self.buttons[i].config(text=" ", fg='black')  # Set text color to black
        else:
            print("Thank you. :) Goodbye!")
            self.root.destroy()

def main():
    root = tk.Tk()
    root.geometry
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()



