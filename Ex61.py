# Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.

def compare(x,y) :
    if x > y :
        return 1
    if x == y :
        return 0
    if x < y :
        return -1
        
a = 1
b = 2
result = compare(a,b)
print(result)