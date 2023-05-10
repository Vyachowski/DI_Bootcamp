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
# 1) Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# 2) Sort the list in alphabetical order.
# 3) Return “Nothing” if you can’t afford anything from the store.

def get_normalized_price(price):
  return int(price.replace('$', '').replace(',', ''))

def get_affordable_items_list (items, wallet):
  affordable_items_list = []
  cash_amount = get_normalized_price(wallet)

  for key, value in items.items():
    price = get_normalized_price(value)
    if price <= cash_amount:
      affordable_items_list.append(key)

  return 'Nothing' if len(affordable_items_list) == 0 else sorted(affordable_items_list)

# Examples
# The key is the product, the value is the price

# Example 1
items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

print(get_affordable_items_list(items_purchase, wallet)) # ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

# Example 2
items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

print(get_affordable_items_list(items_purchase, wallet)) # ➞ "Nothing"

# Example 3
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
  }

wallet = "$300"

print(get_affordable_items_list(items_purchase, wallet)) # ➞ ["Bread", "Fertilizer", "Water"]