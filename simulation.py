import pygame
import sys
import itertools
import numpy as np
import math
import time

WHITE = (255, 255, 255)


class Simulation:
    """
    Initiates a simulation iwith the given parameters.

    Parameters
    ----------
    screen_width: int
        Width of pygame display window

    screen_height: int
        Height of pygame display window

    shapes: list[:class: `Shape`]
        List of `Shape` objects which indicate each shape's
        individual properties and coordinates in
        the simulation environment.

    environment: :class: `Environment`
        Environment Obj, stores,updates and creates environmental
        information of additional collidable immovable objects

    forces: :class: `Forces`
        Forces object which is used to calculate and update the velocities
        of objects. Controls which type of forces exists in the simulation.

    sim_time: int
        Indicates the length of the simulation in seconds.
        Setting to `sim_time` to 0 allows it to run until manually stopped.

    Attributes
    -----------

    background_color: tuple[int,int,int]
        Used to specify the background color in RGB format (R,G,B)
        Each value must be between 0-255.

    """

    background_color = (255, 213, 128)  # Light orange

    def __init__(
        self,
        screen_width: int,
        screen_height: int,
        shapes: list = [],
        sim_time: int = 2,
        environment: object = None,
        forces: object = None,
        render: bool = True
    ):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.shapes = shapes
        self.environment = environment
        self.forces = forces
        self.sim_time = sim_time
        self.tile_size = 50
        self.start_time = time.time()
        self.render = render
        self.clock = pygame.time.Clock()
        # Starts pygame instance.
        if self.render:
            pygame.init()
            pygame.display.set_caption('Environment')
            self.screen = pygame.display.set_mode(
                (screen_width, screen_height))
            self._check_initial_conditions()

    def run(self):
        """Runs the simulation"""
        try:
            while self.running:
                self.clock.tick(20)
                self._check_events()
                if self.render:
                    self._update_screen()
        except BaseException:
            self.running = False
        return [shape.center for shape in self.shapes]

    def _check_time(self):
        """Checks the time elapsed"""
        if self.sim_time:
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.sim_time:
                return True

    def _check_initial_conditions(self):
        """Checks if certain prerequisite conditions are met before
        running a simulation.

        Currently checks to make sure:
            there's only 1 type of moving shape included
            The environment matches the grid-size
            The initial moving objects do not intersect:
        """

        print('Checking Initial Conditions...')
        N_shape_types = len(set([shape.shape for shape in self.shapes]))
        assert N_shape_types == 1, "Multiple types of shapes not currently supported."

        grid_shape = tuple(int(i / self.tile_size)
                           for i in self.screen.get_size())
        assert (self.environment.data.shape ==
                grid_shape), f"Environment size should be {grid_shape}"

        assert (self.forces._collision_forces(self.shapes) ==
                0), "Initial Object positions cannot intersect"
        # todo:Check if outside boundary at IC
        # todo:if any objects overlap surface(s) at IC.
        print("Checking complete.")

    def _check_events(self):
        """Checks and updates the objects positions and velocities.
        Additionally checks if the simulation has reached maximum time. """
        for shape in self.shapes:
            shape.move()
        if self.render:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self._check_time():
                    pygame.display.quit()
                    pygame.quit()
        else:
            if self._check_time():
                self.running = False
        self._check_boundaries()
        if self.environment:
            self.environment.create(self.tile_size)
        self.forces._update_velocities(self.shapes, self.environment.tiles)

    def _update_screen(self):
        """Contains methods which update pygame window"""
        self.screen.fill(self.background_color)
        if self.environment:
            self.environment.draw(self.screen)
        self._draw_grid()
        self._draw_shapes()
        pygame.display.update()

    def _check_boundaries(self):
        """Checks and prevents the moving objects from escaping specified boundary"""
        for shape in self.shapes:
            dy = shape.y + shape.y_vel
            dx = shape.x + shape.x_vel
            if shape.shape == "Circle":
                if dy >= (
                        self.screen_height -
                        shape.radius) or dy <= shape.radius:
                    shape.y_vel *= -1
                    shape.is_bouncing = False
                    if shape.y_vel != 0:
                        shape.is_bouncing = True

                if dx >= (
                        self.screen_width -
                        shape.radius) or dx <= shape.radius:
                    shape.x_vel *= -1
            elif shape.shape == "Square":
                if dy >= (self.screen_height - shape.size) or dy <= 0:
                    shape.y_vel *= -1
                if dx >= (self.screen_width - shape.size) or dx <= 0:
                    shape.x_vel *= -1

    def _draw_grid(self):
        """Renders a grid onto the screen"""
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
        """
        Sets the background color of the rendered simulation.

        Parameters
        ----------
        color: tuple[int,int,int]
            Used to specify the background color in RGB format (R,G,B)
            Each value must be between 0-255.
        """

        cls.background_color = color
