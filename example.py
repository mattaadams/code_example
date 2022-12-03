from simulation import Simulation
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.shape import Shape
from environment import Environment
circle1 = Circle(5.0,x_vel=-1,y_vel=1,x=200)

rect1 = Rectangle(8,8,x=50,x_vel=-1,y_vel=1,color=(0,0,255))

rect2 = Rectangle(8,8,x=100,x_vel=1,y_vel=1,color=(0,0,255))

circle2 = Circle(8.0, x=150, x_vel=1,y_vel=1,color=(120,120,120))


env_data = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
        ]

sim = Simulation(300,300,0,[rect1,rect2],environment=Environment("Test",env_data)) 
sim.run()





