def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
    
a = input("What word do you want to search? ") 
b = input("What letter do you want to find? ") 
c = int(input("What index do you want to start searching at? "))

print(find(a,b,c))