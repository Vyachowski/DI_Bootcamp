# --- 🌟 Exercise 3 : Dogs Domesticated --- #

# Instructions:
# 1) Create a new python file and import your Dog class from the previous exercise.
# 2) In the new python file, create a class named PetDog that inherits from Dog.
# 3) Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# 4) Add the following methods:
#    – train: prints the output of bark and switches the trained boolean to True
#    – play: takes a parameter which value is a few names of other Dog instances (use *args). 
#      The method should print the following string: “dog_names all play together”.
#    – do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#      * “dog_name does a barrel roll”.
#      * “dog_name stands on his back legs”.
#      * “dog_name shakes your hand”.
#      * “dog_name plays dead”.

# IMPORT

from main import Dog
import random

# CODE

class PetDog(Dog):
  def __init__(self, name, age, weight, trained = False):
    super().__init__(name, age, weight)
    self.trained = trained
  
  def train(self):
    print(self.bark())
    self.trained = True

  def play(self, *dogs):
    text_start = ''
    dogs_list = list(map(lambda dog : dog.name, list(dogs))) + [self.name]
    for dog in dogs_list: text_start += f'{dog} '
    return text_start + 'all play together'

  def do_a_trick(self):
    tricks = [' does a barrel roll', ' stands on his back legs', ' shakes your hand', ' plays dead']
    if self.trained: return self.name + random.choice(tricks)

# Instances
dog = PetDog('Caesar', 5, 20)
eric = PetDog('Eric', 4, 32)
chipinkos = PetDog('Chipinkos', 3, 400)

# OUTPUT

print(dog.name)
print(dog.play(eric, chipinkos))

eric.train()
print(eric.do_a_trick())