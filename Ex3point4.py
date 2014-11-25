def do_twice(f,x):
    f(x)
    f(x)
	
def print_spam(y):
    print('spam')

def print_twice(phrase):
	print(phrase)
	print(phrase)

def do_four(fo,val):
    do_twice(fo,val)
    do_twice(fo,val)
	
do_four(print_twice,'spam')
print('')