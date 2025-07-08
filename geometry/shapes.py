from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass 
        #Compute area of the shape


class Square(Shape):
    def __init__(self, side: float):
        self.side = side
        # store side length

    def area(self) -> float:
        return self.side ** 2
        # return side**2

class Circle(Shape):
   def __init__(self, radius: float):
       # store radius
       self.radius = radius

   def area(self) -> float:
       return math.pi * self.radius**2
       # return math.pi * radius**2