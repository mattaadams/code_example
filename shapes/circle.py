from .shape import Shape
import math

class Circle(Shape):
    """
    Implements a circular shape.

    Name
    ----------
    name: string
        Name of circle object

    radius: float
        Radius of circle, 

    """

    def __init__(self,radius:float,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.shape = "Circle"
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        if (radius <= 0):
            raise ValueError("Radius must be above 0")
        self.__radius = radius

    @property
    def area(self):
        return math.pi * self.__radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self.__radius

    @property
    def mass(self):
        return self.density * self.area

    @property
    def width(self):
        return self.radius * 2
        
    @property
    def height(self):
        return self.radius * 2
    
    def __str__(self):
        return f'Circle {self.name}'

