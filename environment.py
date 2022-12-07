import pygame
import numpy as np

BLACK = (0, 0, 0)


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
        data: np.ndarray,
        name: str = "Environment",
    ):

        self.data = data
        self.name = name
        self.tiles = []

    def create(self, tile_size: int):

        self.tiles = []

        for i, row in enumerate(self.data):
            for j, tile in enumerate(row):
                if tile == 0:
                    continue
                if tile == 1:
                    x = j * tile_size
                    y = i * tile_size
                    color = BLACK
                    tile = (color, pygame.Rect((x, y), (tile_size, tile_size)))
                    self.tiles.append(tile)
    def draw(self, screen: object):
            if self.tiles:
                for tile in self.tiles:
                    pygame.draw.rect(screen, tile[0], tile[1])


    def update(self):
        pass

    def __str__(self):
        return f"Environment {self.name}"
