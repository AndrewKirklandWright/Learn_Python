def count(word,letter) :
    count = 0
    for char in word:
        if char ==letter:
            count = count + 1
    print("There are",count, "instances of ",letter)

word = input("What word do you want to search? ") 
letter = input("What letter do you want to count? ")
count(word,letter)