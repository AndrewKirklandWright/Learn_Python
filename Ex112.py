def histogram1(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
    
def histogram2(s):
    d = dict()
    for c in s:
        i = d.get(c,0)
        d[c] = i + 1
    return d
    
a = histogram1('brontosaurus')
print(a)
a = histogram2('brontosaurus')
print(a)