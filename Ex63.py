#Exercise 6.3. Write a function is_between(x, y, z) that returns True if x  y  z or False otherwise.

def is_between(x,y,z) :
    return y <= z and y>= x
    

print(is_between(1,4,3))
