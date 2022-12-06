# code sample -- simple simulations

## About

This repo contains code which
allows you to perform simple simulations with different shapes:

The main `Simulation` class enables the user to run and visualize simple physical interactions.

## Usage

To run a simulation, 
one must first specify a set of parameters:


```
parameters{
        "screen_width": int,                # Pygame window pixel width
        "screen_height": int,               # Pygame window pixel height
        "sim_time": int,                    # Simulation time in seconds
        "render": bool,                     # Renders a visable window of the simulation.
        
        list["circle" : { 
            "name" : str,                   # Name identifier for circle
            "radius" : float,               # Radius of circle in pixels
            "x" : int,                      # X-coordinate of circle
            "y" : int,                      # Y-coordinate of circle
            "density" : float,              # Density of circle
            "x_vel" : float,                # x-velocity of circle in pixel/time
            "y_vel" : float,                # y-velocity of circle in pixel/time
            "color" : tuple[int,int,int],   # Color of circle (R,G,B) format
            },],

            "Environment" :  { 
                "name" : str,               # String indentifier of environment
                "data" : ndarray            # Array of values [0,1] 
                },
            
            "Forces" : {
                "collision" : bool          # Enables collision of objects
                "surface" : bool            # Enables collision between obj and env
                "gravity" : bool            # Enables gravity force on obj
                "magnetic" : bool           # WIP
                "rotation" : bool           # WIP
            }

```

Once your parameters are specified,
the following code can be used to run your simulation.
```
from simulation import Simulation

sim = Simulation(parameters)

sim.run()

```

## Libraries Required

- PyGame 2.1.2
- NumPy 1.22.3
  
## Setup

1. Ensure conda is up-to-date: ```conda update conda```
2. Create and activate new conda environment
3. run ```git clone https://github.com/mattaadams/code_example.git```
4. run ```cd code_example```
5. run ```pip install -e .```