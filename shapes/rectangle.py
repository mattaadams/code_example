from .shape import Shape
import pygame

class Rectangle(Shape):

    def __init__(self,name,height:int,width:int,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.shape = "Rectangle"
        self.name = name
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        if (height <= 0):
            raise ValueError("height must be above 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        if (width <= 0):
            raise ValueError("Width must be above 0")
        self.__width = width

    @property
    def area(self):
        return self.__height * self.__width

    @property
    def perimeter(self):
        return 2 * self.__height + 2 * self.__width

    @property
    def mass(self):
        return self.density * self.area
    
    def __str__(self):
        return f'Rectangle {self.name}'
   