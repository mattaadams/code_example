import numpy as np
from simulation import Simulation
from shapes.circle import Circle
from environment import Environment
from forces import Forces

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
# Tests obj-obj collisions with gravity forces

radius = 10
screen_size = 300

circles = []
for i in range(5):
    circles.append(Circle(10.0, x=50 * (i + 1), y=250, x_vel=1,
                   y_vel=3 * (i + 1), color=(0, 100, 0)))

list_of_shapes = circles
env_data = np.zeros((6, 6))
env1 = Environment(env_data)
force1 = Forces(gravity=True)

sim = Simulation(
    screen_width=screen_size,
    screen_height=screen_size,
    sim_time=10,
    shapes=list_of_shapes,
    environment=env1,
    forces=force1
)

final_positions = sim.run()

all_coordinates = np.concatenate(final_positions,axis=0)

print(all_coordinates)

def test_final_pos_in_bounds():
    assert np.any(all_coordinates < screen_size-radius) == True

    assert np.any(all_coordinates > radius) == True


