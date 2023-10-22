# import random
# import name of file
# random.randint

# import random as r
# r.randint

# from random import randint, choice
# from name of file import name of function

from review_dog_file import Dog
#  from the file import the Dog class
dog1 = Dog("brown", "chihuahua", 3)
dog2 = Dog("white", "malinoa", 5)
# print("dog1", dog1)
# print("dog2", dog2)

print("dog2", dog2.__dict__)
dog1.show()
dog2.show()

john_dog = Dog("brown", "chihuahua", 3)
sara_dog = Dog("white", "german shepard", 5)
tom_dog = Dog("black", "malinoa", 10)

best_breed = "german shepard"
john_dog.check_breed(best_breed)

john_dog.get_oldest_dog(sara_dog)
sara_dog.get_oldest_dog(tom_dog)

# self is john_dog
# other_dog is sara_dog