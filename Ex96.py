"""Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?"""

def is_abecedarian_word (word) :
    i = 0
    for i in range(len(word)-1) :
        if word[i]>word[i+1] :
            return False
    return True
    
    
count = 0
count_total = 0
fin = open('words.txt')
maxlen = 0
for line in fin :
    line = fin.readline()
    word = line.strip()
    count_total = count_total + 1
    if is_abecedarian_word(word) :
        print(word)
        count = count + 1
        if len(word)>maxlen :
            maxlen = len(word)
print(count/count_total * 100, '%,',count,'words')
print('The maximum abcecerdarian word length is',maxlen)