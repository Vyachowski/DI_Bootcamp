# Tic-tac-toe game
# Instructions:
# 1) display_board() – To display the Tic Tac Toe board (GUI).
# 2) player_input(player) – To get the position from the player.
# 3) check_win() – To check whether there is a winner or not.
# 4) play() – The main function, which calls all the functions created above.

# Board:
# def display_board():
#   line = '*  ' + ' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3 + '  *'
#   even_line= line.replace(' ', '-')
#   border = '*' * 17
#   print('*' * 17)
#   print('*  ' + ' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3 + '  *')
#   print('*  ' + '-' * 3 + '|' + '-' * 3 + '|' + '-' * 3 + '  *')
#   print('*  ' + ' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3 + '  *')
#   print('*  ' + '-' * 3 + '|' + '-' * 3 + '|' + '-' * 3 + '  *')
#   print('*  ' + ' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3 + '  *')
#   print('*' * 17)

def display_board():
  even_line = '*  ' + '-' * 3 + '|' + '-' * 3 + '|' + '-' * 3 + '  *'
  line = even_line.replace('-', ' ')
  border = '*' * 17
  print(border)
  print(line)
  print(even_line)
  print(line)
  print(even_line)
  print(line)
  print(border)
display_board()

# line = '*  ' + ' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3 + '  *'
# even_line= line.replace(' ', '-')

# print(line)
# print(even_line)