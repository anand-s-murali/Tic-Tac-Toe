import random

def minimax(board, turns, maximizing):
    # base case
    score = checkWinner(board)
    if score == 0:
        return 100,-1,-1
    elif score == 1:
        return -100,-1,-1
    elif turns == 9:
        return 0,-1,-1

    # otherwise perform recursion
    if maximizing:
        value = -1000
        r_ = -1
        c_ = -1
        # iterate over board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if we can place piece
                if board[i][j] == 46:
                    # place piece and recurse
                    board[i][j] = 88
                    temp_value, r_dummy, c_dummy = minimax(board, turns+1, not maximizing)

                    # re-place piece and check if we maximized
                    board[i][j] = 46
                    if temp_value > value:
                        value = temp_value
                        r_ = i
                        c_ = j

        # return best result
        return value,r_,c_
    else:
        value = 1000
        r_ = -1
        c_ = -1
        # iterate over board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if we can place piece
                if board[i][j] == 46:
                    # place piece and recurse
                    board[i][j] = 79
                    temp_value, r_dummy, c_dummy = minimax(board, turns+1, not maximizing)

                    # re-place piece and check if we maximized
                    board[i][j] = 46
                    if temp_value < value:
                        value = temp_value
                        r_ = i
                        c_ = j

        # return best result
        return value,r_,c_

def getMove(board, turns, player, maximizing):
    # perform minimax search for computer
    _, row, col = minimax(board, turns, maximizing)

    # update board
    board[row][col] = player

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

def showBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("{} ".format(chr(board[i][j])),end="")
        print()

def main():
    # create the board and other necessary variables
    board = [[46,46,46], [46,46,46], [46,46,46]]
    players_list = [79, 88] 
    player = random.choice(players_list) 
    turns = 0
    winner = -1

    while turns < 9 and winner == -1:
        # play the game here
        showBoard(board)
        print()
        
        # play the game from both ends using minimax
        getMove(board, turns, player, (player == 88))
        
        # update variables
        player = 79 if player == 88 else 88
        turns += 1
        winner = checkWinner(board)
    
    # display board after game ends
    showBoard(board)
    print()

    # declare winners/losers
    if winner == 0:
        print("X's won!")
    elif winner == 1:
        print("O's won!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
