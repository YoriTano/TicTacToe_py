import random

def display_board(board):
    print("\nGame Board")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("-----------------------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------------------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    pass

def marker_choice():
    player1_marker = input ("Player 1, choose 'X' or 'O': ").upper()
    if player1_marker != 'X':
        player1_marker = 'O'
    player2_marker = 'X' if player1_marker == 'O' else 'O'
    return player1_marker, player2_marker
    

def place_marker(board, marker, position):  # current board list, which marker, place where
    board[position] = marker
    pass

def has_won(board, marker):
    winning_combinations = [
        [7,8,9], [4,5,6], [1,2,3], #Rows
        [7,4,1], [8,5,2], [9,6,3], #Columns
        [7,5,3], [1,5,9]           #Diagonals
    ]
    
    for combo in winning_combinations:
        if all(board[pos] == marker for pos in combo):
            return True
        
    return False

def choose_first():
    return "player 1" if random.randint(0, 1) == 0 else "player 2"


def board_isfull(board):
    return ' ' not in board[1:]

def player_choice(board):
    while True:
        try:
            position = int(input("Choose a position (1-9:"))
            if 1 <= position <= 9 and board[position] == ' ':
                return position
            else:
                print("Invalid position. Please choose an available position")
        except ValueError:
            print("Invalid input. Please enter a number.")

def replay():
    return input ("Do you want to play again? (yes/no): ").lower().startswith('y')

def yes_no():
    return input("Enter 'yes' or 'no':").lower().startswith('y')
    

def winning_message(winner):
    print(f"Congratulations, {winner} wins!")

def display_keypad():
    print("\nPosition Keypad:")
    print("7 | 8 | 9")
    print("----------")
    print("4 | 5 | 6")
    print("----------")
    print("1 | 2 | 3")

def instructions():
    '''
    print basic game instructions
    feel free to modify
    :return: None
    '''
    print("\nWelcome to Tic Tac Toe!️❌⭕")
    print("Each player  takes turns choosing a position on the board.🎲")
    print("your marker according to the following keypad layout:")
    print("The fisrst player to get three in a row (horizontal, vertical or diagonally)wins!")
    display_keypad()

def play_TicTacToe():
    '''
    The main controller
    Do not modify this function in order to earn full credits of this project
    You must use this function as the main control to get full credits
    You may modify but must submit as additional versions - just for fun, no credits and for future demostration and teaching
    :return:
    '''
    # print game instructions
    print("    *** Welcome to our Tic Tac Toe game! ***    ")
    instructions()

    while True:  #each iteration is one full game/exit if wish not play again
        print("A few questions before we start!")
        the_board = [' '] * 10

        # set player markers
        player1_marker, player2_marker = marker_choice()  # tuple unpacking
        print("Okay, Player 1's marker is '" + player1_marker + "', player 2's marker is '" + player2_marker + "', and", end=" ")

        # who goes first - randomly decide
        # simulate flip coin which player goes first by calling choose_first() which will return "player 1" or "player 2"
        turn = choose_first()
        print(turn + " will go first!")

        # why need to ask "Ready to play?"
        # we will use a boolean gameon to signify if a game is on
        # when there is a win or tie, gameon will be set to false, wait to see if starts another game
        # as user if ready, confirm, set gameon to true until a win or tie set gamon to false
        print("Ready to play?", end=" ")
        gameon = yes_no()  # boolean control one game, ini here

        # game play
        while gameon:  # unless win or tie
            # -----------------player 1's turn--------------------
            if turn == "player 1":  # could switch on 0, or 1, here to be clear
                # 1, display the board by calling display_board(board)
                display_board(the_board)

                # 2, player choose a position by calling player_choice(board)
                print("Player 1 ('" + player1_marker, end="') ")  # reminder the player's current marker choice, nicer message folowing by " choose a position
                position = player_choice(the_board)

                # 3, place the marker on the position by calling place_marker(board, marker, position)
                place_marker(the_board, player1_marker, position)

                # 4, check if they won, or check if it's a tie, else player 2's turn
                # to check if the player has won, by calling haswon(board, mark)
                # to check if it's a tie, by checking if the board if full, by calling board_isfull(board):
                # no tie and no win? next player's turn
                if has_won(the_board, player1_marker):
                    winning_message("PLAYER 1")
                    display_board(the_board)
                    gameon = False
                elif board_isfull(the_board):
                    print("TIE GAME")
                    display_board(the_board)
                    gameon = False
                else:
                    turn = "player 2"
            # --------------------player 2's turn-------------------
            else:  # player 2's turn
                # 1, display the board by calling display_board(board)
                display_board(the_board)

                # 2, player choose a position by calling player_choice(board)
                print("Player 2 ('" + player2_marker, end="') ")
                # print("Player 2", end = " ")
                position = player_choice(the_board)

                # 3, place the marker on the position by calling place_marker(board, marker, position)
                place_marker(the_board, player2_marker, position)  ####change here!

                # 4, check if they won, or check if it's a tie, else player 2's turn
                # to check if the player has won, by calling haswon(board, mark)
                # to check if it's a tie, by checking if the board if full, by calling board_isfull(board):
                # no tie and no win? next player's turn
                if has_won(the_board, player2_marker):  ####change here!
                    winning_message("PLAYER 2")
                    display_board(the_board)
                    gameon = False
                elif board_isfull(the_board):
                    print("Tie game")
                    display_board(the_board)
                    gameon = False
                else:
                    turn = "player 1"  ####change here!
        # --------------------------------
        # single exit the game
        # break out of the while loop on replay()
        
        if not replay():
            
            print("Thank you. :) Goodbye!")
            break #end the program

    # end while loop

# ----------------------------------
def main():
    play_TicTacToe()

if __name__ == "__main__":
    main()