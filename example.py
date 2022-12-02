from simulation import Simulation
from shapes.circle import Circle
from shapes.rectangle import Rectangle

circle1 = Circle("Circle1",5.0,x=200)


rect1 = Rectangle("Square1",8,8,x=50,color=(0,0,255))

rect2 = Rectangle("Square2",8,8,x=100,color=(0,0,255))

circle2 = Circle("Circle1",5.0, x=150, x_vel=10,color=(120,120,120))


sim = Simulation(300,300,1,[circle2]) 
sim.run()

