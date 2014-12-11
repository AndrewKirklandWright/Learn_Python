from math import pi
from math import sin
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

print(bob)
t = bob
length = 100
slices = 16
angle = 360/slices/2     
lt(t,angle)
edge = 2*length*sin(angle/180*pi)

for i in range (slices) :
    fd(t,length)
    lt(t,angle+90)
    fd(t,edge)
    lt(t,angle+90)
    fd(t,length)
    lt(t,180)
wait_for_user()
