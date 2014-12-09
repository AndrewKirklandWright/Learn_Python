"""Exercise 6.7. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case."""

def is_power(a,b) :
#    print(a,b)
    if a==b :
        return True
#        print("1",a,b)
    if a%b == 0 and is_power(a/b,b) :
#        print("2",a,b)
        return True
    return False    

a = 16
b = 2

print (is_power(a,b))

        
