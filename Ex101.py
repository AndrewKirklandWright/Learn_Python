"""Exercise 10.1. Write a function called nested_sum that takes a nested list of integers and add up
the elements from all of the nested lists."""
def nested_sum1(fist) :
    i = 0
    grand_total = 0
    for i in fist :
        print(i)
        total = sum(i)
        print("list = ",i,"sum = ", total)
        grand_total += total
    print("Grand total is ", grand_total)
    
boo = [[1,2,3],[4],[5,6],[7,8,9,10]]    
nested_sum1(boo)