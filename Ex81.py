"""Exercise 8.1. Write a function that takes a string as an argument and displays the letters backward,
one per line."""

def rev(word) :
    i = 1
    while i <= len(word) :
        print(word[-i])
        i = i + 1

getit = input("What word do you want to print backwards? ")        
rev(getit)