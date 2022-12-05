import math
import numpy as np


class Shape:

    """
    Base class for shapes; Implements base-properties 

    WARNING: This class should not be used directly. Use derived classes instead!

    Parameters:
    ----------
    x: int
        x-coordinate of shape.

    y: int
        y-coordinate of shape.

    density: float
        density of the shape: mass units/area

    elasticity: float

    charge: float

    x_vel: float
        x-component of velocity of object: 
            positive velocity is right direction
            negative velocity is left direction

    y_vel: float
        y-component of velocity of object: 
            positive velocity is downward direction
            negative velocity is upward direction

    color: tuple
        Color of the shape

    is_moving: bool


    """

    def __init__(
        self,
        name: str = "Shape",
        x: int = 20,
        y: int = 20,
        density: float = 1.0,
        elasticity: float = 1.0,
        charge: float = 0.0,
        x_vel: float = 0.0,
        y_vel: float = 0.0,
        color: tuple = (0, 255, 0),
        is_moving: bool = True
    ):

        self.name = name
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.charge = charge
        self.color = color
        self._density = density
        self._elasticity = elasticity
        self.is_moving = is_moving

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, density):
        if (density <= 0):
            raise ValueError("Density must be above 0")
        self._density = density

    @property
    def elasticity(self):
        return self._elasticity

    @elasticity.setter
    def elasticity(self, elasticity):
        if (0 < elasticity) or (elasticity > 1):
            raise ValueError("Elasticity must be between [0,1]")
        self._elasticity = elasticity

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    @property
    def forcefield(self):
        pass

    @property
    def vel(self):
        return np.array((self.x_vel, self.y_vel))
