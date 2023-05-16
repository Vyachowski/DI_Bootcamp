class Employee :
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job, emp_salary) :
        self.firstname = emp_fn
        self.lastname = emp_ln
        self.age = emp_age
        self.job = emp_job
        self.salary = emp_salary

    def get_fullname(self) :
        fullname = self.firstname + " " + self.lastname
        return fullname
    
    def happy_birthday(self) : 
        self.age += 1
    
    def get_promotion(self, promotion_amount) :
        self.salary += promotion_amount

    def __str__(self) :
        return f"The Employee : {self.firstname} {self.lastname} {self.age} years old {self.job} {self.salary} shekels"

    def __gt__(self, other) :
        if self.salary > other.salary :
            return self.firstname
        else :
            return other.firstname
        # return self.name if self.salary > other.salary else other.name
    
    def __add__(self, other) :
        return self.salary + other.salary
    
