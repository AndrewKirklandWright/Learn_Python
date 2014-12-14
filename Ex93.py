"""Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?"""

def avoid (word, strlet) :
    for i in strlet :
        if i in word :
            return False
    return True
    
count = 0
count_total = 0
strlet = input("Enter forbidden letters:")
fin = open('words.txt')
for line in fin :
    line = fin.readline()
    word = line.strip()
    count_total = count_total + 1
    if avoid(word,strlet) :
        print(word)
        count = count + 1
print(count/count_total * 100, '%')

