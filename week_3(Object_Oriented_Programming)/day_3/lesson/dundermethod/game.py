from employee import Employee

emp1 = Employee("Lea", "Smith", 30, "developer", 30000)
print(emp1)
# The Employee : Lea Smith 30 developer 30000
emp2 = Employee("John", "Doe", 20, "teacher", 20000)

print(emp1 > emp2) # Lea

print(emp1 + emp2) #50000