import pygame
import sys
import itertools
import numpy as np
import math

WHITE = (255, 255, 255)


class Simulation:
    """
    Simulation summary

    Parameters
    ----------
    screen_width: int
        Name of circle object

    screen_height: int
        Name of circle object

    shapes: list[:class:`Shapes Objects`]

    environment: :class:`Environment Object`

    forces: :class: `Forces Object`

    Attributes
    -----------

    background_color: tuple 
        Used to specify the background color in RGB format (R,G,B)
        Each value must be between 0-255.

    """

    background_color = (255, 213, 128)  # Light orange

    def __init__(
        self,
        screen_width: int,
        screen_height: int,
        shapes: list = [],
        environment=None,
        forces=None
    ):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.shapes = shapes
        self.environment = environment
        self.forces = forces
        self.tile_size = 50

        # Starts pygame instance.
        pygame.init()
        pygame.display.set_caption('Environment')
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

    def run(self):
        self._check_initial_conditions()
        while self.running:
            self.clock.tick(30)
            self._check_events()
            self._update_screen()

    def _check_initial_conditions(self):
        print('Checking Initial Conditions...')

        N_shape_types = len(set([shape.shape for shape in self.shapes]))
        assert N_shape_types == 1, "Multiple types of shapes not currently supported."

        grid_shape = tuple(int(i/self.tile_size)
                           for i in self.screen.get_size())
        assert (self.environment.data.shape ==
                grid_shape), f"Environment size should be {grid_shape}"

        # Check if outside boundary or if any objects overlap at IC.
        print("Checking complete.")

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self._check_boundaries()
        self.forces.collision_forces(self.shapes)
        self.forces.surface_forces(self.shapes, self.environment.tiles)
        for shape in self.shapes:
            shape.move()

    def _update_screen(self):
        self.screen.fill(self.background_color)
        if self.environment:
            self.environment.create(self.screen, self.tile_size)
        self._draw_grid()
        self._draw_shapes()
        pygame.display.update()

    def _check_boundaries(self):
        for shape in self.shapes:
            if shape.shape == "Circle":
                if shape.y >= (self.screen_height - shape.radius - shape.y_vel) or shape.y <= shape.radius - shape.y_vel:
                    shape.y_vel *= -1
                if shape.x >= (self.screen_width - shape.radius - shape.x_vel) or shape.x <= shape.radius - shape.x_vel:
                    shape.x_vel *= -1
            elif shape.shape == "Square":
                if shape.y >= (self.screen_height - shape.size - shape.y_vel) or shape.y <= -shape.y_vel:
                    shape.y_vel *= -1
                if shape.x >= (self.screen_width - shape.size - shape.x_vel) or shape.x <= -shape.x_vel:
                    shape.x_vel *= -1

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
        """Make a drawing of the shape object(s) on the game screen
        """
        for shape in self.shapes:
            if shape.shape == "Square":
                pygame.draw.rect(self.screen, shape.color,
                                 (shape.x, shape.y, shape.size, shape.size))
            elif shape.shape == "Circle":
                pygame.draw.circle(self.screen, shape.color,
                                   (shape.x, shape.y), shape.radius)
            else:
                raise ValueError("Invalid Shape")

    @classmethod
    def set_background_color(cls, color):
        cls.background_color = color
