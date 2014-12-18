"""Exercise 10.3. Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6]."""

def cum(mylist) :
    newlist = []
    temp = 0
    for i in mylist :
        temp += i
        newlist.append(temp)
    return(newlist)
    
ick = [1,2,3,4,5,6,7,8,9,10]
print(cum(ick))        