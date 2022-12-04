import pygame
import sys

WHITE = (255,255,255)

class Simulation:
    """
    Simulation summary

    Parameters
    ----------
    screen_width: int
        Name of circle object

    screen_height: int
        Name of circle object

    gravity: float

    shapes: list

    environment: tbd

    Attributes
    -----------

    background_color: tuple

    """

    background_color = (255, 213, 128)

    def __init__(
                self,
                screen_width: int,
                screen_height: int,
                gravity:float, 
                shapes: list = [],
                environment = None
                ):
        pygame.init()
        pygame.display.set_caption('Environment')
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.gravity = gravity
        self.shapes = shapes
        self.environment = environment
        self.tile_size = 50

    def run(self):
        while self.running:
            self.clock.tick(30)
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self._check_boundaries()
        self._check_tile_collisions()
        for shape in self.shapes:
            shape.move()
            shape.fall(self.gravity)


    def _update_screen(self):
        self.screen.fill(self.background_color)
        if self.environment:
            self.environment.create(self.screen,self.tile_size)
        self._draw_grid()
        self._draw_shapes()
        pygame.display.update()


    def _check_shape_collisions(self):
        for shape in self.shapes:
            x,y = shape.x, shape.y
            
    def _check_tile_collisions(self):
        for tile in self.environment.tiles:
            for shape in self.shapes:
                if shape.shape == "Rectangle":
                    if tile.colliderect(shape.x,shape.y,shape.width,shape.height):
                        print(shape.x,shape.y)
                        print(tile.y)
                        if (shape.y+shape.height) >= tile.y:
                            shape.y_vel *= -1
                        if (shape.y+shape.height) < tile.y:
                            shape.x_vel *= -1





    def _check_boundaries(self):
        for shape in self.shapes:
            if shape.shape == "Circle":
                if shape.y <= shape.radius:
                    shape.y_vel *=-1
                if shape.y >= (self.screen_height - shape.radius):
                    shape.y_vel *=-1
                if shape.x <= shape.radius:
                    shape.x_vel *=-1
                if shape.x >= (self.screen_width - shape.radius):
                    shape.x_vel *=-1
            elif shape.shape == "Rectangle":
                if shape.y <= 0:
                    shape.y_vel *=-1
                if shape.y >= (self.screen_height - shape.height):
                    shape.y_vel *=-1
                if shape.x <= 0:
                    shape.x_vel *=-1
                if shape.x >= (self.screen_width - shape.width):
                    shape.x_vel *=-1
            else:
                raise ValueError("Invalid Shape")
            

    def _draw_grid(self):
        dim = max(self.screen_height, self.screen_width)
        grid_range = dim // self.tile_size
        for line in range(0, grid_range):
            pygame.draw.line(
                self.screen, WHITE,
                (0, line * self.tile_size),
                (dim, line * self.tile_size))
            pygame.draw.line(
                self.screen, WHITE,
                (line * self.tile_size, 0),
                (line * self.tile_size, dim))

    def _draw_shapes(self):
        """Creates a drawing of the shape object(s) on the game screen
        """
        for shape in self.shapes:
            if shape.shape == "Rectangle":
                pygame.draw.rect(self.screen, shape.color, (shape.x, shape.y, shape.width, shape.height))
            elif shape.shape == "Circle":
                pygame.draw.circle(self.screen, shape.color,(shape.x,shape.y),shape.radius)


    @classmethod
    def set_background_color(cls,color):
        cls.background_color = color
        

