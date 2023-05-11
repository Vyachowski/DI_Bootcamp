# Tic-tac-toe game
#
## Instructions:
## 1) The game is played on a grid that’s 3 squares by 3 squares.
## 2) Players take turns putting their marks (O or X) in empty squares.
## 3) The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
## 4) When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

def play():
  mark = 'X'
  other_mark = 'O'
  board = [
    [' '], [' '], [' '],
    [' '], [' '], [' '],
    [' '], [' '], [' '],
  ]
  print('Welcome to TIC TAC TOE!\n')
  for move in enumerate(board):
    display_board()
    print(move)

play()




# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.