# Tic-Tac-Toe
Simple game of tic-tac-toe written and compiled in Golang. Just a basic game to get me started and get a feel for the language, try new things, etc.

# Background
Tic-tac-toe, or Noughts and Crosses, is a simple two player zero-sum game in which the user and computer alternate turns placing their respective piece on the board, each trying to make three in a row. As stated, tic-tac-toe is a classic zero-sum game, which, simply put, means that one player's loss is another player's gain. As a result of this property, we can easily write an algorithm to generate a "smart" computer. Such algorithms include minimax, negamax, and alpha-beta pruning. We will use minimax.

# Implementation
The game board is represented as a two-d slice (not an array!). The user, represented by 'X' picks an index from 1 to 9 (inclusive) to place their piece. The computer, represented by O's, utilizes the minimax algorithm to place its piece. Disregarding the minimax algorithm, most of the code is rather trivial, and mostly involves traversing the game board to check for a winner or iterate until the game is determined.

# Minimax
The minimax algorithm is a recursive finite lookahead algorithm in which the player attempts to maximize their score, and the computer attempts to minimize the score (hence the zero-sum). It does so by considering all possible game trees and ranking the results; really, it is playing all possible games from the given board, and determines what game board has the "best" result. Since tic-tac-toe has a relatively small board, its state space is relatively small (~255168 possible games exist) and can be traversed quite easily. More information can be found https://en.wikipedia.org/wiki/Minimax.

# Other Zero-Sum Games
+ Connect-4
+ Mancala
+ Penny Game
