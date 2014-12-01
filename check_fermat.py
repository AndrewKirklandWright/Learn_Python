def check_fermat(a,b,c,n) :
    if int(a) != a :
        print("'a' must be an integer, try again!")	
    elif int(b) != b :
        print("'b' must be an integer, try again!")	
    elif int(c) != c :
        print("'c' must be an integer, try again!")	
    elif int(n) != n :
        print("'n' must be an integer, try again!")	
    elif n <= 2 :
        print ("'n' must an integer, 3 or greater, try again with larger 'n'")
    elif n<=2 :
        print("'n' is not greater than 2!")	
    elif a**n + b**n != c**n and n>2 :
        print("Fermat was right on that one at least....")
    elif a**n + b**n == c**n and n>2:
        print("Holy smokes, Fermat was wrong!")

a = input("Enter an integer for 'a' = ")
b = input("Enter an integer for 'b' = ")
c = input("Enter an integer for 'c' = ")
n = input("Enter an integer greater than 2 for 'n' = ")

check_fermat(a,b,c,n)		