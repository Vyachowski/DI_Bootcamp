from anagram_checker import AnagramChecker

### IN MY VERSION SCORE BOARD AND EXIT ARE NOT RELATED. SHOWING SCORE BOARD DOESN'T LEAD TO THE EXIT. ###

from game import Game

def get_user_menu_choice():
  user_menu = '\
  Menu:                 \n\n\
    (e) Enter a word \n\
    (x) Exit            \n\
  '
  user_choice = None

  print(user_menu)
  user_choice = input('Your word: ')
  if user_choice == 'e':
    return 'enter'
  elif user_choice == 'x':
    return 'exit'
  else:
    return None
  
def print_results(results):
  print(f"\n\
  ***********************\n\
  Your word: {results['word']}\n\
  This is a valid english word \n\
  Anagrams for your word: {results['anagrams']}\n\
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
