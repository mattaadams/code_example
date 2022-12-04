from simulation import Simulation
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.shape import Shape
from environment import Environment

rect1 = Rectangle(10,10,x=50,x_vel=-5,y_vel=5,color=(0,255,255))

rect2 = Rectangle(40,40,x=100,x_vel=2,y_vel=4,color=(255,0,0))

rect3 = Rectangle(30,50,x=100,y=200,x_vel=4,y_vel=4,color=(150,155,120))

# circle1 = Circle(5.0,x_vel=-1,y_vel=1,x=200)
# circle2 = Circle(8.0, x=150, x_vel=1,y_vel=1,color=(120,120,120))

import numpy as np

env_data = np.zeros((6,6))


sim = Simulation(300,300,0,[rect1,rect2,rect3],environment=Environment(env_data)) 
sim.run()






