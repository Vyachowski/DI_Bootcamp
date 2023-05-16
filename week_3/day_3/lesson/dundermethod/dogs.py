class Dog :

    def __init__(self, a, x, y, w):
        self.name = a
        self.color = x
        self.breed = y
        self.age = w

    # a nice string
    # inform the user of the object
    # work with the file
    def __str__(self) : #str dunder method is to display a informative sentence about the object
        sentence  = f"{self.name} is a {self.color} {self.breed}"
        return sentence

    # a way to represent the object to the developer
    # work with shell
    def __repr__(self) :
        sentence = f"Dog - {self.name} {self.color} {self.breed}"
        return sentence
    
    def __gt__(self, other_dog):
        if self.age > other_dog.age :
            return self.name
        else :
            return other_dog.name
        
    def __add__(self, other_dog) :
        new_breed = f"{self.breed}-{other_dog.breed}"
        new_puppy = Dog(input("puppy name \n"), "black", new_breed, 0)
        return new_puppy

john_dog = Dog("Rex", "brown", "chihuhua", 3)
sara_dog = Dog("Lola", "black", "malinoa", 5)
print(john_dog) #--> str method will be called

print("The oldest dog is ", john_dog > sara_dog) #compare them to know which one is the oldest
puppy = john_dog + sara_dog
# puppy is equal to a Dog object 
# print(object) and if the __str__ method is implemented
print(puppy) # --> calling automaticaly the str method