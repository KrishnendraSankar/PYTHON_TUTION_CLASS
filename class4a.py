################# LIST #################
number = [1,2,3,4,5,6,7,8]
mylist = [1,2,"tuhin",True]

print(number[4])
print(mylist[2])
print(number[-1])
mylist[1] = mylist[1]*10
print(mylist)
mylist.append(30)
print(mylist)

del number[4]
print(number)

number.remove(3)
print(number)

mylist.insert(1, "Banana")
print(mylist)

################### SORT #######################
unsortedlist = [6,3,8,2,9,7,1]
unsortedlist.sort(reverse = True)
print(unsortedlist)

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()
print(guests)

################### SLICING ####################
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors[1:4])

print(colors[-1])
print(colors[:4])
print(colors[6:])
print(colors[-3:])
print(colors[::2])
print(colors[::-1])
print(len(colors))


###################### LIST COPY #######################
dupcolors = colors.copy()
print(dupcolors)
colors[1] = "pink"
print(colors)
print(dupcolors)

#################### LIST JOIN ########################
list1 = [1,2,3]
list2 = [4,5]
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)