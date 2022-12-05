import pandas as pd
import numpy as np
from simulation import Simulation
from shapes.circle import Circle
from environment import Environment
from forces import Forces

circles = []

for i in range(4):
    circles.append(Circle(10.0, y=50 * (i + 1), x=250, y_vel=1,
                   x_vel=3 * (i + 1), color=(0, 100, 0)))

list_of_shapes = circles
env_data = np.zeros((6, 6))

env1 = Environment(env_data)
force1 = Forces(gravity=False)

sim = Simulation(
    screen_width=300,
    screen_height=300,
    shapes=list_of_shapes,
    environment=env1,
    forces=force1
)

fp = sim.run()

print('d')
obj = pd.read_pickle('output.pkl')

print(obj)
