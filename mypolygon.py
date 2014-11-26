from TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001
print(bob)

def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

def polygon(t,n,length):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)		

def circle(t,r):
    n=500
    length = 2*pi*r/n
    for i in range(n):
        fd(t,length)
        lt(t,360/n)	

def arc(t,r,a):
    n=500
    length = 2*pi*r/n
    for i in range(int(n*a/360)):
        fd(t,length)
        lt(t,360/n)

def slice(t,r,a):
    n=500
    length = 2*pi*r/n
    for i in range(int(n*a/360)):
        fd(t,length)
        lt(t,360/n)
    lt(t,360*(a/360))
    fd(t,r)
		
#l=10
#sidenos = 12
#square(bob,l)
#polygon(bob,sidenos,l)
radius = 40
#circle(bob,radius)
angle = 180
#arc(bob,radius,angle)
slice(bob,radius,angle)
wait_for_user()