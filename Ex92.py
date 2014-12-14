"""Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it. Modify your program from the previous section to print only the words that have no “e” and compute
the percentage of the words in the list have no “e.”"""

def has_no_letter_e(word) :
    for letter in word :
        if letter == 'e':
            return False
    return True

#print(has_no_letter_e('tsst'))    
    
fin = open('words.txt')
count_total = 0
count_e = 0
for line in fin :
    line = fin.readline()
    word = line.strip()
    if has_no_letter_e(word) :
        count_e = count_e + 1
        #print(word)
    count_total = count_total + 1
print (count_e/count_total * 100, "% of words have no letter 'e'.")
        