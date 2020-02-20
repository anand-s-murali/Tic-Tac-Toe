import random
'''
userMove places the user's piece at the specified location
'''
def userMove(board, pos):
    # check that pos is in the valid range
    if pos < 0 or pos > 9:
        print("Please enter a valid number in the range 1 to 9 to place your piece.")
        return False
    
    # compute row and col
    row = pos // 3
    col = pos % 3

    # check that the spot isn't already taken
    if board[row][col] != 46:
        print("That position is already taken! Please choose another position.")
        return False

    # otherwise update board
    board[row][col] = 88
    return True

'''
minimax performs the minimax algorithm, looking for the best move for the computer.
'''
def minimax(board, depth, turns, maximizing):
    # base case
    score = checkWinner(board)
    if score == 0:
        return 100000,-1,-1
    elif score == 1:
        return -100000,-1,-1
    elif turns == 9:
        return 0,-1,-1
    
    # otherwise perform recursion
    if maximizing:
        value = -1000000
        r_ = -1
        c_ = -1
        # iterate over board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if we can place piece
                if board[i][j] == 46:
                    # place piece and recurse
                    board[i][j] = 88
                    temp_value, r_dummy, c_dummy = minimax(board, depth+1, turns+1, not maximizing)

                    # re-place piece and check if we maximized
                    board[i][j] = 46
                    if temp_value > value:
                        value = temp_value
                        r_ = i
                        c_ = j

        # return best result
        return value,r_,c_
    else:
        value = 1000000
        r_ = -1
        c_ = -1
        # iterate over board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if we can place piece
                if board[i][j] == 46:
                    # place piece and recurse
                    board[i][j] = 79
                    temp_value, r_dummy, c_dummy = minimax(board, depth+1, turns+1, not maximizing)

                    # re-place piece and check if we maximized
                    board[i][j] = 46
                    if temp_value < value:
                        value = temp_value
                        r_ = i
                        c_ = j

        # return best result
        return value,r_,c_

'''
findMove is almost like a helper fucntion; it finds the computer's next move via minimax and places the piece at the position.
'''
def findMove(board, turns):
    # perform minimax search for computer
    _, row, col = minimax(board, 0, turns, False)

    # update board
    board[row][col] = 79

'''
checkWinner searches for a winner in the game: 0 for player, 1 for computer, -1 if draw
'''
def checkWinner(board):
    # check rows and columns simultaneously in order rows or cols.
    for i in range(len(board)):
        if (board[i][0] == 88 and board[i][1] == 88 and board[i][2] == 88) or (board[0][i] == 88 and board[1][i] == 88 and board[2][i] == 88):
            return 0
        elif (board[i][0] == 79 and board[i][1] == 79 and board[i][2] == 79) or (board[0][i] == 79 and board[1][i] == 79 and board[2][i] == 79):
            return 1


    # check diagonals in order main or anti
    if (board[0][0] == 88 and board[1][1] == 88 and board[2][2] == 88) or (board[0][2] == 88 and board[1][1] == 88 and board[2][0] == 88):
        return 0
    elif (board[0][0] == 79 and board[1][1] == 79 and board[2][2] == 79) or (board[0][2] == 79 and board[1][1] == 79 and board[2][0] == 79):
        return 1
    
    # we have a draw
    return -1
 
'''
showBoard displays the game board.
'''
def showBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("{} ".format(chr(board[i][j])),end="")
        print()

'''
main is where the game is played.
'''
def main():
    # perform basic game instructions for the user
    print("Welcome to Tic-Tac-Toe, a fun game for all ages! In this implementation, you will be facing the computer! Be aware, if you don't play optimally, the computer will :)")
    print("You, the player, will be marked by X's on the board, while the computer will be marked by O's. When it is your turn to make a move, please enter a numerical")
    print("digit in the range [1,9] (brackets for inclusion) to place your piece.")
    print("\n")
    
    # create the board and other necessary variables
    board = [[46,46,46], [46,46,46], [46,46,46]]
    player = random.randint(0,2)
    turns = 0
    winner = -1
    allowed_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
   
    if player == 0:
        print("You will begin the game.")
    else:
        print("The computer will begin the game.")

    while winner == -1:
        # play the game here
        showBoard(board)
        print()
        
        if player == 0:
            pos = -1
            success = False
            while not success:
                pos = input("Please enter a number in the range 1 to 9 (inclusive) to place your piece. ")
                if pos not in allowed_input:
                    continue
                success = userMove(board, int(pos)-1)
        else:
            # perform minimax
            findMove(board, turns)
        
        # update variables
        if player == 0:
            player = 1
        else:
            player = 0
        turns += 1
        winner = checkWinner(board)
        
        # special case for out of moves
        if turns == 9 and winner == -1:
            break
    
    # display board after game ends
    showBoard(board)
    print()
    
    # declare winners/losers
    if winner == 0:
        print("Congrats! You won!")
    elif winner == 1:
        print("Sorry! You lost! Better luck next time!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
