class AnagramChecker:
  def __init__(self, words_list):
    # read a file and convert it to a list with strings in lowercase
    self.words_list = list(map(lambda x: x.lower(), open(words_list, "r").read().splitlines()))

  def is_valid_word(self, word):
    if word.uppper() in self.words_list:
      return True
    else:
      return False
  
  def get_anagrams(self, word):
    result = []
    for value in self.words_list:
      if sorted(word) == sorted(value):
        if word != value:
          result.append(value)
    return result

example = './week_3/day_5/exercises/anagram_checker/sowpods.txt'
ana = AnagramChecker(example)
result = ana.get_anagrams('meat')
print(result)
