### IN MY VERSION SCORE BOARD AND EXIT ARE NOT RELATED. SHOWING SCORE BOARD DOESN'T LEAD TO THE EXIT. ###

from game import Game

def get_user_menu_choice():
  user_menu = '\
  Menu:                 \n\n\
    (g) Play a new game \n\
    (s) Show score      \n\
    (x) Exit            \n\
  '
  user_choice = None

  print(user_menu)
  user_choice = input('Your choice: ')
  if user_choice == 'g':
    return 'game'
  elif user_choice == 's':
    return 'score'
  elif user_choice == 'x':
    return 'exit'
  else:
    return None
  
def print_results(results):
  print(f"\n\
  ***********************\n\
  Game results: \n\
  You won  {results['win']} times \n\
  You lose {results['loss']} times\n\
  You drew {results['draw']} times\n\n\
  Thank you for playing!\n\
  ***********************\n")

def main():
  game = Game()
  user_choice = None
  score_board = {'win': 0, 'loss': 0, 'draw': 0}
  
  while user_choice != 'exit':
    user_choice = get_user_menu_choice()

    if user_choice == 'score':
      print_results(score_board)
    elif user_choice != 'exit':
      result = game.play()

      if result == 'win':
        score_board['win'] += 1
      elif result == 'loss':
        score_board['loss'] += 1
      elif result == 'draw':
        score_board['draw'] += 1
  print_results(score_board)

# OUTPUT

main()