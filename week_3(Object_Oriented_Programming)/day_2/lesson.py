class Employee:
  def __init__(self, firstname, lastname, age, job, salary):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.job = job
    self.salary = salary

  def get_fullname(self):
    return f"{self.firstname} {self.lastname}"

  def happy_birthday(self):
    self.age += 1

  def get_promotion(self, promotion_amount):
    self.salary += promotion_amount

  def show_info(self):
    print(f"Name: {self.get_fullname()}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}")


lea = Employee("Lea", "Smith", 30, "developer", 50000)
david = Employee("David", "Schartz", 20, "teacher", 40000)

# OUTPUT 
lea.happy_birthday()
lea.get_promotion(10000)
lea.show_info() # -> Name: Lea Smith, Age: 31, Job: developer, Salary: 60000

david.happy_birthday()
david.get_promotion(5000)
david.show_info() # -> Name: David Schartz, Age: 21, Job: teacher, Salary: 45000

class Developer(Employee):
  def __init__(self, firstname, lastname, age):
    super().__init__(firstname, lastname, age, job="developer", salary=15000)
    self.coding_skills = []

  def add_skills(self, *skills):
    self.coding_skills.extend(skills)

  def coding(self):
    print(f"{self.get_fullname()} knows the following coding languages: {', '.join(self.coding_skills)}")

  def coding_with_partner(self, other_developer):
    print(f"{self.get_fullname()} and {other_developer.get_fullname()} are coding together.")
    print(f"{self.get_fullname()} knows: {', '.join(self.coding_skills)}")
    print(f"{other_developer.get_fullname()} knows: {', '.join(other_developer.coding_skills)}")

  def get_promotion(self, promotion_amount):
    self.salary *= promotion_amount

tom = Developer("Tom", "Cruiz", 30)
angelina = Developer("Angelina", "Jolie", 23)

# OUTPUT 
tom.add_skills("Python", "JavaScript", "Java") # -> Tom Cruiz knows the following coding languages: Python, JavaScript, Java
tom.coding()
tom.coding_with_partner(angelina) # -> Tom Cruiz and Angelina Jolie are coding together...
tom.get_promotion(1.2)
tom.show_info() # -> Name: Tom Cruiz, Age: 30, Job: developer, Salary: 18000.0

angelina.add_skills("C++", "Ruby") # -> Angelina Jolie knows the following coding languages: C++, Ruby
angelina.coding() 
angelina.coding_with_partner(tom) # -> Angelina Jolie and Tom Cruiz are coding together...
angelina.get_promotion(1.5)
angelina.show_info() # -> Name: Angelina Jolie, Age: 23, Job: developer, Salary: 22500.0