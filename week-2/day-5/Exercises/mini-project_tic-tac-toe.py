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

def display_board():
  board_name = 'TIC TAC TOE'
  border = '* ' * 9
  line = lambda row_num : f'*   {board[row_num][0]} | {board[row_num][1]} | {board[row_num][2]}   *'
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
  current_mark = mark if step % 2 == 0 else other_mark
  print(f'Player {current_mark}\'s turn...')
  while succesful_step == False:
    row = -1
    while not row in range(0,3):
      try:
        answer = int(input("Enter row: "))
        row =  answer - 1
      except:
        print('Are you serious? Letters?')
    column = -1
    while not column in range(0,3):
      try:
        answer = int(input("Enter column: "))
        column = answer - 1
      except:
        print('No way, buddy. Only numbers from 1 to 3.')
    if board[row][column] == ' ':
      board[row][column] = current_mark
      succesful_step = True
    else:
      print('Sorry, this square is already taken. Choose another one...')

def check_win():
  player_1_win_condition =  mark * 3
  player_2_win_condition =  other_mark * 3

  diagonal_1 = ''.join([board[0][0], board[1][1], board[2][2]])
  diagonal_2 = ''.join([board[0][2], board[1][1], board[2][0]])

  transposed_board = list(zip(*board))
  result_board = board + transposed_board

  if (diagonal_1 or diagonal_2) == player_1_win_condition:
    return 'Player 1 has won!'
  elif (diagonal_1 or diagonal_2)  == player_2_win_condition:
    return 'Player 2 has won!'
  
  for row in result_board:
    line = ''.join(row)
    if line == player_1_win_condition:
      return 'Player 1 has won!'
    elif line == player_2_win_condition:
      return 'Player 2 has won!'
  return ''

# GAME

def play():
  
  print('Welcome to TIC TAC TOE!\n')
  for step, *rest in enumerate([item for sublist in board for item in sublist]):
    display_board()
    player_input(step)
    win_status = check_win()
    if len(win_status) > 0:
      display_board()
      return print(win_status)
  display_board()
  print('Friendship!')

# RUN GAME

play()