class Student :

    city = "Paris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student name is {self.name}, Student age is {self.age} years old"
    
    @staticmethod
    def check_grade(grade):
        if grade > 80 :
              return "A"
        else :
              return "B"
    
    @classmethod
    def create_high_school_student(cls,age) :
         if age >= 15 :
            new_student = cls("Emma", age)
            return new_student
    
    @classmethod
    def change_city(cls) :
        cls.city ="New York"


class Student_Tlv(Student):
     
    city = "TLV"

student1 =  Student.create_high_school_student(17)
print(student1.city)
Student.change_city()
print(student1.city)

studentTLV = Student_Tlv.create_high_school_student(16)
print(studentTLV)
print(studentTLV.city)










# student1 = Student("John", 13)
# result = Student.check_grade(86)
# print(result)

# function that creates a new high school student 
# so its age must be > 15

# static method
# @staticmethod

# decorator
# @classmethod


# --> modify a class attribute
# --> or to create new objects

# create a function
# check the grade --> 80 --> A
#                 --> 60 --> B

# def check_grade(grade):
#     if grade > 80 :
#         return "A"
#     else :
#         return "B"