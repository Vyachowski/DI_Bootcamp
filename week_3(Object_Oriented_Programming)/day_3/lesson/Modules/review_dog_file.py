# box contains attributes and methods
# attributes define an object
class Dog :

    def __init__(self, x, y, w):
        self.color = x
        self.breed = y
        self.age = w

    def show(self) :
        print(f"The dog is a {self.color} {self.breed}")
    
    def check_breed(self, best) :
        if self.breed == best :
            print("The dog is the best")
        else :
            print("The dog is not the best")

    def get_oldest_dog(self, other_dog) :
        # print(other_dog) # an object
        if self.age > other_dog.age :
            print(f"the first dog is higher")
        else :
            print(f"the second dog is higher")
        
