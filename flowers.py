from TurtleWorld import *

from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001
print(bob)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t,length,angle) :	
    arc(t,length,angle)
    lt(t,180-angle)
    arc(t,length,angle)
    lt(t,180-angle)
    lt(t,360/nos_petals)
	
def flower(t,length,nos_petals,angle) :
	for i in range(nos_petals) :
	    petal(t,length,angle)
angle = 90	
nos_petals = 3
length = 100

flower(bob,length,nos_petals,angle)

wait_for_user()

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60, 60)

move(bob, 100)
flower(bob, 10, 40, 80)

move(bob, 100)
flower(bob, 20, 140, 20)

die(bob)

# dump the contents of the campus to the file canvas.eps
world.canvas.dump()

