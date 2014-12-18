"""Exercise 9.7. This question is based on a Puzzler that was broadcast on the radio program Car
Talk (http: // www. cartalk. com/ content/ puzzlers ):
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-
p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?"""

def consec (word) :
    i = 0
    count = 0
    if len(word) < 6 :
        return False
    while i < (len(word)-5) :
        if word[i] == word [i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True
        i = i + 1
    return False
            
fin = open('words.txt')
for line in fin :
    line = fin.readline()
    word = line.strip()
    if consec(word) :
        print(word)

