import math
import numpy as np


class Shape:

    """
    Base class for shapes; Implements base-properties

    WARNING: This class should not be used directly. 
    Use or create derived classes instead!

    Parameters:
    ----------
    x: int
        x-coordinate of shape.

    y: int
        y-coordinate of shape.

    density: float
        density of the shape: mass units/area

    x_vel: float
        x-component of velocity of object:
            positive velocity is right direction
            negative velocity is left direction

    y_vel: float
        y-component of velocity of object:
            positive velocity is downward direction
            negative velocity is upward direction

    color: tuple[int,int,int]
        Color of the shape

    """

    def __init__(
        self,
        name: str = "Shape",
        x: int = 20,
        y: int = 20,
        density: float = 1.0,
        x_vel: float = 0.0,
        y_vel: float = 0.0,
        color: tuple[int, int, int] = (0, 255, 0),
    ):

        self.name = name
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self._density = density
        self.is_bouncing = True

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, density):
        if (density <= 0):
            raise ValueError("Density must be above 0")
        self._density = density

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.y_vel < 0:
            self.is_bouncing = True
        return (self.x, self.y)

    @property
    def vel(self):
        return np.array((self.x_vel, self.y_vel))
