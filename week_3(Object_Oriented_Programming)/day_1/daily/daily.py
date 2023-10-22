# --- OLD MACDONALD’s FARM --- #

# 1) Create the code that is needed to receive the result. Below are a few questions to assist you with your code:
# 2) Create a class called Farm. How should it be implemented?
#    – Does the Farm class need an __init__ method? If so, what parameters should it take?
#    – How many methods does the Farm class need?
#    – Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
#    – Test your code and make sure you get the same results as the example above.
#    – Bonus: nicely line the text in columns as seen in the example above. Use string formatting.
# 3) Expand The Farm:
#    – Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. 
#      With the example above, the list should be: ['cow', 'goat', 'sheep'].
#    – Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. 
#      The method should call the get_animal_types function to get a list of the animals.
# Expected:
# McDonald's farm
# cow : 5
# sheep : 2
# goat : 12
# E-I-E-I-0!

class Farm:
  def __init__(self, farm_name):
    self.owner = farm_name
    self.slogan = 'E-I-E-I-0!'
    self.animals = {}
  
  def add_animal(self, animal, amount = 1):
    self.animals.setdefault(animal, 0)
    self.animals[animal] += amount
  
  def get_animal_types(self):
    return sorted(list(self.animals.keys()))
  
  def get_short_info(self):
    animals_list = self.get_animal_types()
    animals_text_nobody = 'There are no animals on the farm now'
    animals_text = f'McDonald’s farm has '
    for animal in animals_list: animals_text += f'{animal}s, '
    animals_text_corrected = (animals_text.replace(",", " and", 1))[:-2]
    return animals_text_corrected if len(animals_list) > 0 else animals_text_nobody
  
  def get_info(self):
    welcome_text = (f'{self.owner} \'s farm\n\n')
    slogan_text = '\n\t' + self.slogan
    animals_text = ''
    for key, value in self.animals.items(): animals_text += f'{key} : {value} \n'
    return welcome_text + animals_text + slogan_text

  
mcdonald = Farm('McDonald')
mcdonald.add_animal('cow',5)
mcdonald.add_animal('sheep')
mcdonald.add_animal('sheep')
mcdonald.add_animal('goat', 12)
print(mcdonald.get_info())
print(mcdonald.get_animal_types())
print(mcdonald.get_short_info())