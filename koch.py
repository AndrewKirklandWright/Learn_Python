from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.000001

def koch_curve (t,x):
    if x < 3:
        fd(t,x)
    else :
        koch_curve(t,x/3)
        lt(t,60)
        koch_curve(t,x/3)
        rt(t,120)
        koch_curve(t,x/3)
        lt(t,60)
        koch_curve(t,x/3)

length = 81*3
koch_curve(bob,length)
rt(bob,120)
koch_curve(bob,length)
rt(bob,120)
koch_curve(bob,length)
rt(bob,120)
wait_for_user()