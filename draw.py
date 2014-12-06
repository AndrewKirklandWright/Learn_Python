from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

def draw(t, length, n):
    if n == 0:
        return
    angle = 30
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)
    
draw(bob,6,8)
wait_for_user()