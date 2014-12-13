def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word,letter) :
    count = 0
    i = 0
    while i < len(word) :
        i = find(word,letter,i)
        if i == -1 :
            break
        count = count + 1
        i = i + 1
    print("There are",count, "instances of ",letter)

word = input("What word do you want to search? ") 
letter = input("What letter do you want to count? ")
count(word,letter)