"""Write a function called estimate_pi that uses this formula to compute and return an estimate of
p. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10􀀀15). You can check the result by comparing it to math.pi."""

def estimate_pi () :
    import math
    k = 0
    sum = 0
    c = 2*math.sqrt(2)/9801
    while True :
        t = math.factorial(4*k)*(1103+26390*k)/math.factorial(k)**4/396**(4*k)
        #print(t)
        sum = sum + t
        pie = 1/c/sum
        if t < 0.0000000000000001 :
            print(k)
            print(pie)
            break
        k = k + 1
           
estimate_pi()