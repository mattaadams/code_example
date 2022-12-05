import pygame
import math
import itertools
import numpy as np


class Forces:
    """
    collision: bool

    surface: bool

    gravity: bool

    magnetic: bool

    rotation: bool
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

    def collision_forces(self, objects):
        if self.collision:
            for obj1, obj2 in itertools.combinations(objects, 2):
                if obj1.shape == obj2.shape == "Square":
                    rect1 = pygame.Rect((obj1.x, obj1.y), (obj1.size, obj1.size))
                    if rect1.colliderect(obj2.x, obj2.y, obj2.size, obj2.size):
                        self._collide(obj1, obj2)

                if obj1.shape == obj2.shape == "Circle":
                    distance = math.sqrt((obj2.x - obj1.x)**2 + (obj2.y-obj1.y)**2)
                    if distance <= (obj1.radius + obj2.radius):
                        self._collide(obj1, obj2)

    def _collide(self, obj1, obj2):
        # Adapted from https://en.wikipedia.org/wiki/Elastic_collision
        M = obj1.mass + obj2.mass
        norm = np.linalg.norm(obj1.center-obj2.center)**2
        v1 = obj1.vel - ((2*obj2.mass)/M) * (np.dot(obj1.vel-obj2.vel,
                                             obj1.center-obj2.center) / norm) * (obj1.center-obj2.center)

        v2 = obj2.vel - ((2*obj1.mass)/M) * (np.dot(obj2.vel-obj1.vel,
                                             obj2.center-obj1.center) / norm) * (obj2.center-obj1.center)
        obj1.x_vel = v1[0]
        obj1.y_vel = v1[1]

        obj2.x_vel = v2[0]
        obj2.y_vel = v2[1]

    def surface_forces(self, objects, surfaces):
        for surface in surfaces:
            for obj in objects:
                if obj.shape == "Rectangle":
                    if surface.colliderect(obj.x, obj.y+obj.y_vel, obj.size, obj.size):
                        obj.y_vel *= -1
                    if surface.colliderect(obj.x+obj.x_vel, obj.y, obj.size, obj.size):
                        obj.x_vel *= -1
                if obj.shape == "Circle":
                    pass

    def gravity_forces(self, objects):
        for obj in objects:
            obj.y_vel -= 1

    def magnetic_forces(self):
        pass

    def rotational_forces(self):
        pass

    def summation_forces(self):
        pass

