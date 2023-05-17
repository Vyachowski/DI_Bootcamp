# --- Daily Challenge - Circle --- #
# Instructions :
# 1) The goal is to create a class that represents a simple circle.
#    – A Circle can be defined by either specifying the radius or the diameter.
#    – The user can query the circle for either its radius or diameter.
# 2) Other abilities of a Circle instance:
#    – Compute the circle’s area
#    – Print the circle and get something nice
#    – Be able to add two circles together
#    – Be able to compare two circles to see which is bigger
#    – Be able to compare two circles and see if there are equal
#    – Be able to put them in a list and sort them

# IMPORT

import math

# CODE

class Circle:
    def __init__(self, radius = None, diameter = None):
      if radius is not None:
        self.radius = radius
        self.diameter = self.radius * 2
      elif diameter is not None:
        self.diameter = diameter
        self.radius = diameter / 2
      else:
        raise ValueError("Enter radius or diameter in the specified format: 'radius=int or diameter=int'")


    @property
    def area(self):
      return math.pi * self.radius ** 2

    def __str__(self):
      return f"Circle with radius: {self.radius}"

    def __add__(self, other):
      if isinstance(other, Circle):
        return Circle(radius=self.radius + other.radius)
      else:
        raise TypeError('Unssupported input. You can add only two circles')

    def __gt__(self, other):
      if isinstance(other, Circle):
        return self.radius > other.radius
      else:
        raise TypeError('Unssupported input. You can compare only two circles')

    def __eq__(self, other):
      if isinstance(other, Circle):
        return self.radius == other.radius
      else:
        raise TypeError('Unssupported input. You can compare only two circles')

    def __lt__(self, other):
      if isinstance(other, Circle):
        return self.radius < other.radius
      else:
        raise TypeError('Unssupported input. You can compare only two circles')

# OUTPUT

# Create circles
circle1 = Circle(radius=3)
circle2 = Circle(diameter=6)

# Query properties
print(circle1.radius)     # ->  3
print(circle2.diameter)   # ->  6

# Compute area
print(circle1.area)       # ->  28.274333882308138

# Print circle
print(circle2)            # ->  Circle with radius: 3.0

# Add circles
circle3 = circle1 + circle2
print(circle3.radius)     # ->  6

# Compare circles
print(circle1 > circle2)  # ->  False
print(circle1 == circle2) # ->  True
print(circle1 < circle2)  # ->  False

# Sort circles
circles = [Circle(3), Circle(2), Circle(4), Circle(1)]
sorted_circles = sorted(circles)
print([circle.radius for circle in sorted_circles])     # ->  [Circle(radius=1), Circle(radius=2), Circle(radius=3), Circle(radius=4)]