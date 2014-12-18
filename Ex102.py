"""Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized."""

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res   

def capitalise_nested(nestedlistofstrings) :
    veryluck = []
    for i in nestedlistofstrings :
        veryluck.append(capitalize_all(i))
    return veryluck

    
luck = [['a','b','c'],['d'],['e','f'],['g','h','i','j']]    
print(capitalise_nested(luck))
