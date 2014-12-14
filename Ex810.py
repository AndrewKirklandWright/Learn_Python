"""Exercise 8.10. A string slice can take a third index that specifies the “step size;” that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 6.6."""

def is_pal(word) :
    if word == word[::-1] :
        print("Yes, this is a palendrome.")
    else :
        print("No,this is not a palendrome.")

word = input("Enter the word: ")        
is_pal(word)