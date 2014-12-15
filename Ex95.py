"""Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?"""

def uses_all_letters (word, lttrs) :
    for index in lttrs :
        if (index in word) == False :
            return False
    return True
    
    
count = 0
count_total = 0
let = input('Entura letters:')
fin = open('words.txt')
for line in fin :
    line = fin.readline()
    word = line.strip()
    count_total = count_total + 1
    if uses_all_letters(word,let) :
        print(word)
        count = count + 1
print(count/count_total * 100, '%,',count,'words')