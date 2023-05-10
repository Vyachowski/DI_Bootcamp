# CHALLENGE 1
# 1) Ask a user for a word
# 2) Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
#    - Make sure the letters are the keys.
#    - Make sure the letters are strings.
#    - Make sure the indexes are stored in a list and those lists are values.

def word_to_dictionary(word):
  dictionary = {}
  for position, letter in enumerate(word):
    if letter not in dictionary:
      dictionary[letter] = [position]
    else:
      dictionary[letter].append(position)
  print(dictionary)

# Examples
word_to_dictionary('dodo')
word_to_dictionary('froggy')

# CHALLENGE 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

# ➞ "Nothing"
