import pygame
import numpy as np

BLACK = (0,0,0)

class Environment:

    """
    Parameters
    ----------

    data: ndarray
        2D array containing data with `float` type.
        Data represents the environment where
        
    name: str
        Name of environment

    """
    def __init__(
                self,
                data:np.ndarray,
                name:str="Environment",
                ):

        self.data = data
        self.name = name
        self.tiles = []


    def create(self,screen,tile_size):

        grid_shape = tuple(int(i/tile_size) for i in screen.get_size())
        assert (self.data.shape == grid_shape), f"Environment size should be {grid_shape}"

        self.tiles = []
        for i,row in enumerate(self.data):
            for j, tile in enumerate(row):
                if tile == 0:
                    continue
                if tile == 1:
                    x = j * tile_size
                    y = i * tile_size
                    color = BLACK
                    tile = (color, pygame.Rect((x, y), (tile_size, tile_size)))
                    pygame.draw.rect(screen, tile[0], tile[1])
                    self.tiles.append(tile[1])


    def update(self):
        pass


    def __str__(self):
        return f"Environment {self.name}"
