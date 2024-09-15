def add(x=1,y=0):
    z = x+y
    print(z)

add(x=10, y=12)


################ LAMBDA EXPRESSION ################
def name(first, last):
    return f"{first} {last}"

print(name("Vikas", "Tripathi"))
##########################################

def outerName(first, last, nameGenerator):
    return nameGenerator(first, last) 

print(outerName("Vikas", "Tripathi", lambda first,last: f"{first} {last}"))

def times(n):
    return lambda x: x*n 
double = times(2)
triple = times(3)
print(double(2))
print(triple(4))


