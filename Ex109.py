"""Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original. Hint: they don’t have to be in the same order."""

def remove_dups (ilist) :
    newlist = sorted(ilist) 
    n = len(ilist)
    print(n)
    for i in range (n-1) :
        print(i)
        if newlist[i+1] == newlist[i] :
            s = newlist[i]
            j = 0
            for j in range (len(newlist)-1) :
                print('    ',j)
                if newlist[j] == s :
                    newlist.remove(s)
                    print(newlist)
                if j+1 >= len(newlist) :
                    break
        if i+1 >= len(newlist) :
            break
    ilist = newlist
t = ['a','b','d','d','d']
print( t )
remove_dups(t)
print(t)

