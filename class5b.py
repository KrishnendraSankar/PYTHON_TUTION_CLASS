#SETS

s1 = {1,2,3,4,5,6,1}

print(s1)

# Unordered, Unchangable, No Duplicate Values

for i in s1:
    print(i)

print(5 in s1)
print(8 in s1)
print(7 not in s1)

s1.add(7)
print(s1)

s2 = {8,9,10,11,12}

s1.update(s2)
print(s1)

s1.remove(11)
print(s1)

s1.discard(10)
print(s1)

s1.discard(14)

s1.pop()
print(s1)

s4 = {"apple","samsung","motorola"}
print(s4)
s4.clear()
print(s4)

s5 = {23,346,123}
print(s5)
del s5
print(s5)


