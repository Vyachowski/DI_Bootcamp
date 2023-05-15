# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:
# 1) Create another cat breed named Siamese which inherits from the Cat class.
# 2) Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# 3) Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# 4) Take all the cats for a walk, use the walk method.
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
bengal = Bengal('Bingo', 4)
chart = Chartreux('Chat', 4)
siam = Siamese('Siam', 4)

all_cats = [bengal, chart, siam]
sara_pets = Pets(all_cats)
sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# Instructions:
# 1) Create a class called Dog with the following attributes name, age, weight.
# 2) Implement the following methods in the Dog class:
# 3) bark: returns a string which states: “<dog_name> is barking”.
# 4) run_speed: returns the dogs running speed (weight/age*10).
# 5) fight : takes a parameter which value is another Dog instance, called other_dog. 
#    – This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
# 6) Create 3 dogs and run them through your class.
class Dog:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight

  def bark(self):
    print(f'{self.name} is barking!')

  def run_speed(self):
    return self.weight/self.age*10

  def fight(self, other_dog):
    return f'Dog {self.name if self.run_speed() > other_dog.run_speed() else other_dog.name} has won the fight by a TKO!'

davids_dog = Dog('Rex', 50, 15)
sarahs_dog = Dog('Teacup', 20, 45)
boris_dog = Dog('Monstr', 2, 95)

# OUTPUT

davids_dog.bark()
print(davids_dog.fight(sarahs_dog))
sarahs_dog.bark()
print(sarahs_dog.fight(davids_dog))
boris_dog.bark()
print(boris_dog.fight(sarahs_dog))

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.