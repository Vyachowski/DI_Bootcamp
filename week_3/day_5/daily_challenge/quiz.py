
# Part 1 : Quizz
# What is a class?
'''Class is a blueprint to create instances. It combines attributes and methods, both are encapsulated from other data'''
# What is an instance?
'''Instance is the implementation of the class'''
# What is encapsulation?
'''Encapsulation is a way to restrict direct access to some data that belongs to a class'''
# What is abstraction?
'''It is a way to hide a big amount of data by one name to reduce complexity of the created system'''
# What is inheritance?
'''It is a property of classes to use a methods or attributes in children of the class'''
# What is multiple inheritance?
'''Multiple inheritance is when children inherit attributes or methods from two or more classes'''
# What is polymorphism?
'''Polymorphism is a way to use a single interface to perform different actions on subclasses'''
# What is method resolution order or MRO?
'''It is a way that programming language use to deal with multiple inheritance. 
   It helps resolve any potential conflicts and provides a consistent way to find methods in the inheritance hierarchy.'''

# Part 2: Deck card

# IMPORT

import random

# CODE
class Card:
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def __repr__(self):
    return f"{self.value} of {self.suit}"

class Deck:
  def __init__(self):
    self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    return self.cards.pop() if self.cards else None

# OUTPUT
deck = Deck()
deck.shuffle()

for _ in range(5):
  card = deck.deal()
  if card:
    print("Dealt card:", card)
  else:
    print("No more cards in the deck.")
