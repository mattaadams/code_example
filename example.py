from simulation import Simulation
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.shape import Shape
from environment import Environment
circle1 = Circle(5.0,x_vel=-1,y_vel=1,x=200)

rect1 = Rectangle(8,8,x=50,x_vel=-4,y_vel=5,color=(0,0,255))



circle2 = Circle(8.0, x=150, x_vel=1,y_vel=1,color=(120,120,120))

import numpy as np

env_data = np.zeros((6,6))
env_data[3] = 1
env_data[3][1:4] = 0


sim = Simulation(300,300,0,[rect1],environment=Environment(env_data)) 
sim.run()

# import pygame
# a = pygame.Rect((1, 1), (10, 10))

# print(a.height)



