class Dog :

    def __init__(self, name_dog, age_dog, dog_energy = 100) :
        self.name = name_dog
        self.age = age_dog
        self.energy =  dog_energy

    def bark(self):
        print(f"{self.name} said Wouaf Wouaf")

    def play(self, type_game="stick"):
        if self.energy < 10 :
            self.sleep()
        else : 
            if type_game == "ball":
                self.energy -= 10
            elif type_game == "stick":
                self.energy -= 5
            else :
                self.energy -= 2
    
    def play_with_other_dog(self, other_dog) :
        #other_dog is an object
        # print(other_dog.__dict__)
        print(f"{self.name} is playing with {other_dog.name}")
        self.energy -= 70
        other_dog.energy -= 50
    
    def sleep(self) :
        self.energy += 50


tom_dog = Dog("King", 7)
# tom_dog is an object of the Dog class
# tom_dog is an instance of the Dog class
lea_dog = Dog("Rex", 4)
lea_dog.bark()
lea_dog.play()

tom_dog.play_with_other_dog(lea_dog)

print(f"{tom_dog.name} energy is {tom_dog.energy}")
print(f"{lea_dog.name} energy is {lea_dog.energy}")