from .shape import Shape
import pygame
import numpy as np


class Square(Shape):
    """
    Implements a square shape.

    Name
    ----------

    size: float
        size of square

    *args: Variable length argument list.

    **kwargs: Arbitrary keyword arguments.

    """

    def __init__(self, size: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shape = "Square"
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (size <= 0):
            raise ValueError("size must be above 0")
        self.__size = size

    @property
    def area(self):
        return self.__size ** 2

    @property
    def perimeter(self):
        return 4 * self.__size

    @property
    def mass(self):
        return self.density * self.area

    @property
    def center(self):
        # PyGame uses topleft corner as x,y coordinates
        center_x = self.x + (self.__size / 2)
        center_y = self.y + (self.__size / 2)
        return np.array((center_x, center_y))

    def __str__(self):
        return f'size {self.__size} Square {self.name}'
