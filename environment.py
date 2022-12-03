import copy
import pygame


BLACK = (0,0,0)

class Environment:

    """
    Parameters
    ----------

    name: str

    data: list[int]

    tile_size: int


    """
    def __init__(
                self,
                name:str,
                data:list[int],
                ):

        self.name = name
        self.data = copy.deepcopy(data)


    def create(self,screen,tile_size):
        for i,row in enumerate(self.data):
            for j, tile in enumerate(row):
                if tile == 0:
                    x = j * tile_size
                    y = i * tile_size
                    color = None
                    tile = (color, pygame.Rect((x, y), (tile_size, tile_size)))
                if tile == 1:
                    x = j * tile_size
                    y = i * tile_size
                    color = BLACK
                    tile = (color, pygame.Rect((x, y), (tile_size, tile_size)))
                    pygame.draw.rect(screen, tile[0], tile[1])


                




    def update(self):
        pass


    def __str__(self):
        return f"Environment {self.name}"
