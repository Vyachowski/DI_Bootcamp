# --- TIC TAC TOE GAME --- #

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

marks = ('X', 'O')

# SERVICE FUNCTIONS

## Show a board
def display_board():
  board_name = 'TIC TAC TOE'
  border = '* ' * 9
  row = lambda row_num : f'*   {board[row_num][0]} | {board[row_num][1]} | {board[row_num][2]}   *'
  divider = '*  ---|---|---  *'

  print(board_name)
  print(border)
  print(row(0))
  print(divider)
  print(row(1))
  print(divider)
  print(row(2))
  print(border)

## Enter the answer
def player_input(step):
  move_is_succesful = False
  current_mark = marks[0] if step % 2 == 0 else marks[1]
  print(f'Player {current_mark}\'s turn...')
  while move_is_succesful == False:
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
      move_is_succesful = True
    else:
      print('Sorry, this square is already taken. Choose another one...')

## Check if one of the player won
def check_win():
  win_conditions = [marks[0] * 3, marks[1] * 3]
  
  diagonals = [''.join([board[0][0], board[1][1], board[2][2]]), 
               ''.join([board[0][2], board[1][1], board[2][0]])]

  transposed_board = list(zip(*board))
  result_board = board + transposed_board

  victory_message = lambda player_num : f'Player {player_num} has won!'

  if win_conditions[0] in diagonals:
    return victory_message(1)
  elif win_conditions[1] in diagonals:
    return victory_message(2)
  
  for row in result_board:
    line = ''.join(row)
    if line == win_conditions[0]:
      return victory_message(1)
    elif line == win_conditions[1]:
      return victory_message(2)
  return ''

# GAME

def play():
  
  print('Welcome to TIC TAC TOE!\n')
  for step, *rest in enumerate([item for sublist in board for item in sublist]): # ugly line, pending changes
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