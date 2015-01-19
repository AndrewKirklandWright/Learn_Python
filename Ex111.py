"""Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary."""


def make_word_list() :
    file_object = open('words.txt') 
    word_list = []
    for line in file_object :
        word = line.strip()
        word_list.append(word)
    return word_list
    

def make_dictionary (word_list) :
    the_dictionary = dict()
    for word in word_list :
        the_dictionary[word] = 'null'
    return the_dictionary
        

thelist = make_word_list()
result = make_dictionary(thelist)
if 'aaa' in result :
    print('True')
else :
    print('False')