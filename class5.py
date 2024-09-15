#TUPLE
#immutable
t1 = (1,'2',4,True)
print(t1[2])

l1 = list(t1) # [1,'2',4,True]
l1[2] = 6
t1 = tuple(l1)
print(t1)

#unpacking
t2 = ("mango", "bmw", "redmi")
(fruits,car,mobile) = t2 #("mango", "bmw", "redmi")

print(fruits)
print(car)
print(mobile)

for i in t1:
    print(i)

t3 = t1+t2
print(t3)

t4 = (1,2,3,1,4,6,3,5,2,4,7,3,9,1,4,3)
count = t4.count(3)
print(count)
position = t4.index(3)
print(position)
