"""Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa?”"""

def uses_only_letters(word, strnglttrs) :
    for i in word :
        if (i in strnglttrs) == False :
            return False
    return True

count = 0
count_total = 0
strlet = 'acefhlo'
fin = open('words.txt')
for line in fin :
    line = fin.readline()
    word = line.strip()
    count_total = count_total + 1
    if uses_only_letters(word,strlet) :
        print(word)
        count = count + 1
print(count/count_total * 100, '%')