import numpy as np
from simulation import Simulation
from shapes.circle import Circle
from shapes.square import Square
from shapes.shape import Shape
from environment import Environment
from forces import Forces
# rect1 = Square(10,x=50,x_vel=-5,y_vel=5,color=(0,255,255))

# rect2 = Square(40,x=100,x_vel=2,y_vel=4,color=(255,0,0))

# rect3 = Square(50,x=100,y=200,x_vel=4,y_vel=4,color=(150,155,120))

circle1 = Circle(10.0, x_vel=-4, y_vel=1, x=200)
circle2 = Circle(17.0, x=150, x_vel=4, y_vel=1, color=(120, 120, 120))
circle3 = Circle(7.0, x=100, x_vel=4, y_vel=1, color=(120, 250, 20))
circle4 = Circle(17.0, x=250, x_vel=4, y_vel=4, color=(250, 20, 120))


env_data = np.zeros((6, 6))
env_data[4] = 1
env1 = Environment(env_data)
force1 = Forces()

sim = Simulation(
    screen_width=300,
    screen_height=300,
    shapes=[circle1, circle2, circle3, circle4],
    environment=env1,
    forces=force1
)
sim.run()
