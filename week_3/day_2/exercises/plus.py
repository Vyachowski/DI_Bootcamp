# --- Exercise 1 : Family --- #

# Instructions:
# 1) Create a class called Family and implement the following attributes:
#    – members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
#    – last_name : (string)
#    * Initial members data:
#    [
#      {'name':'Michael','age':35,'gender':'Male','is_child':False},
#      {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#    ]
# 2) Implement the following methods:
#    born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
#    is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
#    family_presentation: a method that prints the family’s last name and all the members’ first name.

# CODE
class Family:
  def __init__(self, members, last_name):
    self.members = members
    self.name = last_name

  def born(self, **birth_data):
    newborn = {'name': '', 'age': 0, 'gender': '', 'is_child': True}
    newborn.update(birth_data)
    self.members.append(newborn)
    return 'Congratulions! Your family has a new member!'

  def is_18(self, name):
    for member in self.members: 
      if name in member.values(): 
        if member['age'] >= 18: return True
        else: return False
    return None

  def family_presentation(self):
    print(f'It is {self.name} Family\n\nFrom left to right:')
    for member in self.members: print(member['name'])

members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
          ]

# OUTPUT

kuzmini = Family(members, 'Kuzmini')
kuzmini.born(name='Kolya', gender='Male')
print(kuzmini.members)
print(kuzmini.is_18('Michael'))
print(kuzmini.is_18('Sarah'))
print(kuzmini.is_18('Jancarlo'))
kuzmini.family_presentation()

# --- Exercise 2 : The Incredibles Family --- #

# Instructions:
# 1) Create a class called TheIncredibles. This class should inherit from the Family class:
#    – This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
#    – Initial members data:
#    [
#      {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#      {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#    ]
# 2) Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
# 3) Add a method called incredible_presentation which :
#   – Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
#   – Prints all the members’ incredible name and power.
# 4) Call the incredible_presentation method.
# 5) Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6) Call the incredible_presentation method again.
