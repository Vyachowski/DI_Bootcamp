class Dog :
    #class attribute
    amount_dog = 0
    dog_park = "Tlv dog park"
    all_dogs = []

    def __init__(self, a, x, y, w):
        self.name = a
        self.color = x
        self.breed = y
        self.age = w
        Dog.amount_dog += 1
        Dog.all_dogs.append(self)

    def __str__(self) : 
        sentence  = f"{self.name} is a {self.color} {self.breed}"
        return sentence
    
john_dog = Dog("Rex", "brown", "chihuhua", 3)

john_dog.dog_park = "Ramat Gan Park" #modify it

print(john_dog.dog_park) #"Ramat Gan Park"
print(john_dog)

sara_dog = Dog("Lola", "black", "malinoa", 5)

print(sara_dog.dog_park) # "Tel Aviv Park"

print(Dog.all_dogs)

print(Dog.amount_dog) # classattribute so we access it with the class