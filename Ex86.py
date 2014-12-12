def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word,letter) :
    count = 0
    index = 0
    for i in range(len(word)) :
        find(word,letter,index)
        
    print("There are",count, "instances of ",letter)

word = input("What word do you want to search? ") 
letter = input("What letter do you want to count? ")
count(word,letter)