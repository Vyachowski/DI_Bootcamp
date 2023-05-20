example = './week_3/day_5/exercises/anagram_checker/sowpods.txt'

class AnagramChecker:
  def __init__(self, words_list):
    self.words_list = open(words_list, "r").read().splitlines()

  def is_valid_word(self, word):
    if word.uppper() in self.words_list:
      return True
    else:
      return False
  
  def get_anagrams(self, word):
    word_to_uppercase = word.upper()
    result = []
    for value in self.words_list:
      if sorted(word_to_uppercase) == sorted(value):
        if word_to_uppercase != value:
          result.append(value)
    return result


ana = AnagramChecker(example)
result = ana.get_anagrams('MEAT')
print(result)
