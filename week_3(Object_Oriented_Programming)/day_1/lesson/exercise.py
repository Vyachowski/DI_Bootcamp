# --- Exercise 1 --- #

## Intsructions:
## 1) Create a Employee class, With the attributes : 
##    – firstname, lastname, age, job, salary
## 2) Create 2 users object and display their attribute
##    – Lea Smith 30 years old developer 30000
##    – David Schartz 20 years old project manager 20000
## 3) Add those methods to the class
##    – get_fullname(self) : that return the firstname + lastname
##    – happy_birthday(self) : that return the age incremented by one
##    – get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
## 4) Call all the methods

# Create class
class Employee : 
  def __init__(self, firstname, lastname, age, job, salary):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.job = job
    self.salary = salary

  def get_fullname(self):
    return self.firstname + ' ' +  self.lastname

  def happy_birthday(self):
    return self.age + 1

  def get_promotion(self, promotion_amount = 1000):
    return self.salary + promotion_amount

# Create instances
Leah_Smith = Employee('Leah', 'Smith', 30, 'Developer', 30000)
David_Schartz = Employee('David', 'Schartz', 20, 'Project Manager', 20000)

# Example 1
print(Leah_Smith.get_fullname())
print(Leah_Smith.happy_birthday())
print(Leah_Smith.get_promotion(12000))

# Example 2
print(David_Schartz.get_fullname())
print(David_Schartz.happy_birthday())
print(David_Schartz.get_promotion(2000))