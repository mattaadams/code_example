import numpy as np
from ..simulation import Simulation
from ..shapes.circle import Circle
from ..shapes.square import Square
from ..shapes.shape import Shape
from ..environment import Environment
from ..forces import Forces
from ..player import Player

square1 = Square(10, x=50, x_vel=-5, y_vel=5, density=1, color=(0, 255, 255))
square2 = Square(10, x=60, x_vel=2, y_vel=4, color=(255, 0, 0))
square3 = Square(50, x=100, y=200, x_vel=4, y_vel=4, color=(150, 155, 120))

player1 = Player(radius=10, density=1)

circles = []
circles.append(
    Circle(
        10.0,
        name='black',
        x=60,
        y=150,
        x_vel=0,
        y_vel=10,
        color=(
            0,
            0,
             0)))

for i in range(1):
    circles.append(Circle(10.0, name='yellow', x=60 * (i + 1),
                   y=250, x_vel=0, y_vel=5 * (i + 1), color=(255, 255, 128)))

circle1 = Circle(12.0, x=60 * (i + 1), y=50, x_vel=1,
                 y_vel=2 * (i + 1), color=(256, 0, 0))

list_of_shapes = circles
# list_of_shapes = [square1, square2]
env_data = np.zeros((6, 6))
# env_data[4] = 1
env1 = Environment(env_data)
force1 = Forces(gravity=True)

sim = Simulation(
    screen_width=300,
    screen_height=300,
    shapes=list_of_shapes,
    environment=env1,
    forces=force1
)
sim.run()
