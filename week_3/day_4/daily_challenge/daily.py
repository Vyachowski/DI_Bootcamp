# --- Text Analysis --- #
# Part I:
# 1) First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
# 2) Create a class called Text that takes a string as an argument and store the text in a attribute.
#    – Hint: You need to manually copy-paste the text, straight into the code
# 3) Implement the following methods:
#    – a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
#    – a method that returns the most common word in the text.
#    – a method that returns a list of all the unique words in the text.
# Part II:
# 1) Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# 2) Implement a classmethod that returns a Text instance but with a text file:
#    – Text.from_file('the_stranger.txt')
#    – Hint: You need to open and read the text from the text file.
# 3) Now, use the provided the_stranger.txt file and try using the class you created above.

# IMPORT

import os

# CODE

example_string = 'A good book would sometimes cost as much as a good house'
class Text:
  def __init__(self, text):
    self.text = text

  def word_frequency(self, word):
    words = self.text.split()
    count = words.count(word)
    return count
  
  # get is method to get value of the key. Used for convinience
  def most_common_word(self):
    words = self.text.split()
    if not words:
      return None
    word_counts = {}
    for word in words:
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
    most_common_word = max(word_counts, key=word_counts.get)
    return most_common_word
  
  def unique_words(self):
    words = self.text.split()
    unique_words = []
    for word in words:
      if word not in unique_words:
        unique_words.append(word)
    return unique_words
  
  @classmethod
  def from_file(cls, file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_path)
    with open(file_path, 'r') as file:
      text = file.read()
    return cls(text)

# OUTPUT

text = Text(example_string)
text_from_file = Text.from_file('the_stranger.txt')

print(text.unique_words()) # -> ['A', 'good', 'book', 'would', 'sometimes', 'cost', 'as', 'much', 'a', 'house']
print(text_from_file.most_common_word()) # -> the