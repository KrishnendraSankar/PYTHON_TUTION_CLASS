#Iterables

for i in range(5):
    print(i)

str1 = "VIVEKANANDA"
for j in str1:
    print(j)

#ITERATOR
l1 = ["banana", "mango", "grapes"]
l1_iter = iter(l1)

print(next(l1_iter))
print(next(l1_iter))
print(next(l1_iter))

l1_iter_new = iter(l1)
for i in l1_iter_new:
    print(i)


