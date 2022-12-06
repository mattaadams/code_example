import numpy as np
from simulation import Simulation
from shapes.circle import Circle
from environment import Environment
from forces import Forces

# Tests y_velocity-only gravity, collission and boundaries

# Tests collisions between a non-moving object and moving object.

radius = 10
screen_size = 300

circles = []
circles.append(Circle(10.0, x=50, y=200, x_vel=0, y_vel=3, color=(0, 100, 0)))
circles.append(Circle(10.0, x=50, y=100, x_vel=0, y_vel=3, color=(200, 0, 0)))


list_of_shapes = circles
env_data = np.zeros((6, 6))
env1 = Environment(env_data)
force1 = Forces(gravity=True)

sim = Simulation(
    screen_width=screen_size,
    screen_height=screen_size,
    sim_time=20,
    shapes=list_of_shapes,
    environment=env1,
    forces=force1,
    render=False
)

final_positions = sim.run()

all_coordinates = np.concatenate(final_positions, axis=0)


def test_final_pos_in_bounds():
    assert np.all(all_coordinates < screen_size - radius)

    assert np.all(all_coordinates > radius)
