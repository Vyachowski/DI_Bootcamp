# --- GAME LOGIC --- #

import random

class Game:
  '''Simple child game (that called CU-EF-A in Russia) against computer'''

  def __init__(self) -> None:
    self.__move_variants = { 
      'rock': ['rock', 'rok', 'roc', 'r', '1'],
      'paper': ['paper', 'p', '2'],
      'scissors': ['scissors', 'scissor', 'scisors', 'scisors', 's', '3']
      }
    self.__all_moves_list = sum(self.__move_variants.values(), [])

  def get_user_item(self):
    user_variant = ''

    while user_variant not in self.__all_moves_list:
      user_variant = input('Selecet [r]ock, [p]aper or [s]cissors: ') # Maybe need to add a code for printing errors
    user_item = ''.join([key for key, values in self.__move_variants.items() if user_variant in values])
    return user_item
  
  def get_computer_item(self):
    computer_item = random.choice(list(self.__move_variants.keys()))
    return computer_item

  def get_game_result(self, user_item, computer_item):
    if user_item == computer_item:
      return 'draw'
    elif (user_item == 'rock' and computer_item == 'scissors') or \
         (user_item == 'paper' and computer_item == 'rock') or \
         (user_item == 'scissors' and computer_item == 'paper'):
      return 'win'
    else:
      return 'loss'

  def play(self):
    user_item = self.get_user_item()
    computer_item = self.get_computer_item()
    result = self.get_game_result(user_item, computer_item)

    print(f'You selected {user_item}. The computer selected {computer_item}.')

    if result == 'win':
        print('You win!')
    elif result == 'draw':
        print('It\'s a draw!')
    else:
        print('You lose!')

    return result