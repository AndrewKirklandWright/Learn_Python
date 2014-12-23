"""Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return
False."""

def is_inorder (list) :
    i = 0
    while i < len(list)-1 :
        if list[i+1] < list[i] :
            return False
        i = i + 1
    return True
 
getit = ['a','b','c','a']
print(is_inorder(getit))