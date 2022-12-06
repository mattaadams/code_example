import pygame
import math
import itertools
import numpy as np


class Forces:
    """
    Forces object is used to calculate and update 
    the final velocities of objects. Controls which 
    type of forces exists in the simulation.

    Parameters
    ----------
    collision: bool, default True
        Enables Collision forces which update moving object velocities
        upon collision with another movable object.

    surface: bool, default True
        Enables Collision forces which update moving object velocities
        upon colliding with an immovable surface object.

    gravity: bool, default True
        Enables gravity which updates the each moving object's y-velocity

    magnetic: bool, default False
        WIP TODO

    rotation: bool, default False
        WIP TODO
    """

    def __init__(self,
                 collision=True,
                 surface=True,
                 gravity=True,
                 magnetic=False,
                 rotation=False
                 ):
        self.collision = collision
        self.surface = surface
        self.gravity = gravity
        self.magnetic = magnetic
        self.rotation = rotation

    def _collision_forces(self, shapes):
        """
        Two-body interactions between two shape objects.
        Calculates the final velocities for each object after collision.

        Parameters
        ----------

        shapes: list[:class:`Shapes shapes`]
            List of shape objects

        Returns
        -------

        collisions: int
            Total number of collisions across shapes.
        """
        collisions = 0
        for shape_1, shape_2 in itertools.combinations(shapes, 2):
            if shape_1.shape == shape_2.shape == "Square":
                rect1 = pygame.Rect(
                    (shape_1.x, shape_1.y), (shape_1.size, shape_1.size))
                if rect1.colliderect(
                        shape_2.x, shape_2.y, shape_2.size, shape_2.size):
                    self.calculate_final_collision_velocities(shape_1, shape_2)
                    collisions += 1

            if shape_1.shape == shape_2.shape == "Circle":
                distance = math.sqrt(
                    (shape_2.x - shape_1.x)**2 + (shape_2.y - shape_1.y)**2)
                speed = np.abs(shape_1.vel - shape_2.vel)
                collide_speed = math.floor(
                    np.sqrt(speed[0]**2 + speed[1]**2))
                max_comp_speed = max(speed[0], speed[1])
                if distance < (shape_1.radius + shape_2.radius + max_comp_speed):
                    self.calculate_final_collision_velocities(shape_1, shape_2)
                    collisions += 1
            # TODO - implement square-circle interaction
            if shape_1.shape != shape_2.shape:
                raise ValueError("Multiple types of shapes not supported.")
        return collisions

    def calculate_final_collision_velocities(self, shape_1, shape_2):
        """
        Calculates and updates the final velocities when 
        two-movable objects directly collide 

        Parameters
        ----------

        shape_1, shape2: :class: `Shape Object`
            List of `Shape` objects which indicate each shape's 
            individual properties and coordinates in 
            the simulation environment.

        """
        # Adapted from https://en.wikipedia.org/wiki/Elastic_collision
        M = shape_1.mass + shape_2.mass
        norm = np.linalg.norm(shape_1.center - shape_2.center)**2
        if norm == 0:
            norm = 1e6

        if shape_1.is_bouncing == False:
            shape_1.y_vel = 0
            shape_2.y_vel *= -1
        if shape_2.is_bouncing == False:
            shape_2.y_vel = 0
            shape_1.y_vel *= -1

        dot1 = (
            np.dot(
                shape_1.vel -
                shape_2.vel,
                shape_1.center -
                shape_2.center))
        dot2 = (
            np.dot(
                shape_2.vel -
                shape_1.vel,
                shape_2.center -
                shape_1.center))
        final_v1 = shape_1.vel - ((2 * shape_2.mass) / M) * \
            (dot1 / norm) * (shape_1.center - shape_2.center)

        final_v2 = shape_2.vel - ((2 * shape_1.mass) / M) * \
            (dot2 / norm) * (shape_2.center - shape_1.center)

        shape_1.x_vel = math.floor(final_v1[0])

        if shape_2.is_bouncing == True and shape_1.is_bouncing == True:
            shape_1.y_vel = math.floor(final_v1[1])
            shape_2.y_vel = math.floor(final_v2[1])

    def _surface_forces(self, shapes, surfaces):
        """
        Calculates the velocity of object after colliding with environmental
        surface tile object.

        Two-body interactions between a shape and a tile.

        Parameters
        ----------

        shapes: list[:class:`Shape Object`]


        surfaces: list[:class:`PyGame.Rect Object`]


        """
        for surface in surfaces:
            for shape in shapes:
                dy = shape.y + shape.y_vel
                dx = shape.x + shape.x_vel
                if shape.shape == "Rectangle":
                    if surface.colliderect(
                            shape.x, dy, shape.size, shape.size):
                        shape.y_vel *= -1
                    if surface.colliderect(
                            dx, shape.y, shape.size, shape.size):
                        shape.x_vel *= -1
                if shape.shape == "Circle":
                    if surface.colliderect(
                            shape.x, dy, shape.radius, shape.radius):
                        shape.y_vel *= -1
                        shape.is_bouncing = False
                    if surface.colliderect(
                            dx, shape.y, shape.radius, shape.radius):
                        if shape.y_vel < 0:
                            shape.x_vel *= -1

    def _gravitational_forces(self, shapes):
        """

        Applys simple gravity field to shapes, updating velocity.

        Parameters
        ----------
        shapes: list[:class:`Shape Object`]

        """

        for shape in shapes:
            gravity = 1
            if shape.is_bouncing:
                shape.y_vel += gravity

    def _update_velocities(self, shapes, surface):
        """
        Parameters
        ----------

        shapes: list[:class:`Shape Object`]
            List of `Shape` objects which indicate each shape's 
            individual properties and coordinates in 
            the simulation environment.

        surface: :class: `Environment Object`
            Environment Obj, stores,updates and creates environmental 
            information of additional collidable immovable objects

        """

        if self.collision:
            self._collision_forces(shapes)

        if self.surface:
            self._surface_forces(shapes, surface)

        if self.gravity:
            self._gravitational_forces(shapes)
