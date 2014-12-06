def is_triangle (a,b,c) :
# checks to see whether three sticks of lengths a, b, and c can be placed to form a triangle.
    if (a>(b+c)) or (b>(a+c)) or (c>(a+b)) :
        print("No, it's not possible.")
    elif (a==(b+c)) or (b==(a+c)) or (c==(a+b)) :
        print("Degenerate triangle!")
    else :
        print("These sticks can potentially make a triangle.")
        
a1=input("Enter length a = ? ")
b1=input("Enter length b = ? ")
c1=input("Enter length c = ? ")

a2=float(a1)
b2=float(b1)
c2=float(c1)

is_triangle(a2,b2,c2)