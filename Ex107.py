"""Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams."""

def is_ananagram (word1, word2) :
    if len(word1) != len(word2) :
        return False
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    if list1==list2 :
        return True
    else :
        return False

#    i = 0
#    while i < len(list1)-1 :
#        if list1[i] != list2[i] :
#            return False
#        i = i + 1
#    return True
 


boo = open('words.txt')
for line1 in boo :
    line1 = boo.readline()
    word1 = line1.strip()
    fin = open('words.txt')
    for line in fin :
        line = fin.readline()
        word2 = line.strip()
        if word1 == word2:
            break
        elif is_ananagram(word1,word2) :
            print(word1,word2)
