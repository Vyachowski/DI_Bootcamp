# Tic-tac-toe game
#
## Instructions:
## 1) The game is played on a grid that’s 3 squares by 3 squares.
## 2) Players take turns putting their marks (O or X) in empty squares.
## 3) The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
## 4) When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# VARIABLES

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
  ]

mark = 'X'
other_mark = 'O'

# SERVICE FUNCTIONS

def check_win():
  

def display_board():
  board_name = 'TIC TAC TOE'
  border = '* ' * 9
  line = lambda line_num : f'*   {board[line_num][0]} | {board[line_num][1]} | {board[line_num][2]}   *'
  divider = '*  ---|---|---  *'

  print(board_name)
  print(border)
  print(line(0))
  print(divider)
  print(line(1))
  print(divider)
  print(line(2))
  print(border)

def player_input(step):
  succesful_step = False
  current_mark = mark if step % 2 != 0 else other_mark
  print(f'Player {current_mark}\'s turn...')
  while succesful_step == False:
    row = 0
    while not row in range(1,4):
      try:
        row = int(input("Enter row: "))
      except:
        print('Are you serious? Letters?')
    column = 0
    while not column in range(1,4):
      try:
        column = int(input("Enter column: "))
      except:
        print('Are you serious? Letters?')
    if board[row - 1][column - 1] == ' ':
      board[row - 1][column - 1] = current_mark
      succesful_step = True
    else:
      print('Sorry, this square is already taken. Choose another one...')

# GAME

def play():
  print('Welcome to TIC TAC TOE!\n')
  for step, *rest in enumerate([item for sublist in board for item in sublist]):
    display_board()
    player_input(step)
    if check_win() == True:
      print(f'And the winner is {mark}')
      break
  # display_board()
  # print('Friendship!')

# RUN GAME

# play()