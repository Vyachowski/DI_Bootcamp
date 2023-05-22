from anagram_checker import AnagramChecker
import re
example_dict = './week_3/day_5/exercises/anagram_checker/sowpods.txt'

def get_user_menu_choice():
  user_menu = \
  'Menu:               \n\n\
    (e) Enter a word   \n\
    (x) Exit           \n\
  '
  user_choice = None

  print(user_menu)
  user_choice = input('Your choice: ').lower()
  if user_choice == 'e':
    return 'enter'
  elif user_choice == 'x':
    return 'exit'
  else:
    return None
  
def get_user_word():
  word = None
  pattern = r'[^a-zA-Z]'

  while word == None:
    user_variant = input('Your word: ')
    if ' ' in user_variant.strip():
      print('Only one word is allowed!')
    if re.search(pattern, user_variant.strip()):
      print('No numbers and special symbols allowed')
    else:
      word = user_variant.strip().lower()
      return word
  
def print_results(word, anagrams):
  print(f"\n\
  ***********************\n\
  Your word: {word}\n\
  This is a valid english word \n\
  Anagrams for your word: {anagrams}\n\
  ***********************\n")

def main():
  anagram_checker = AnagramChecker(example_dict)
  user_choice = None
  
  while user_choice != 'exit':
    user_choice = get_user_menu_choice()
    
    if user_choice == 'enter':
      valid_word = False

      while valid_word == False:
        word = get_user_word()
        if anagram_checker.is_valid_word(word):
          valid_word = True
        else: print('Such word does not exist!')

      anagrams = anagram_checker.get_anagrams(word)
      print_results(word, anagrams)
    elif user_choice == 'exit':
      return print('Goodbye!')

# OUTPUT

main()