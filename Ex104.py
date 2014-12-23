"""Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3]."""

def middle_of_list (lis) :
    del lis[0]
    del lis[-1]
    
getit = ['a','b','c','d']
print(middle_of_list(getit))
print(getit)