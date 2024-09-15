x = 20
print(type(x))

print(type(str(x)))
print(type(float(x)))
print(x)
y = float(x)
print(y)

#COMPARISON OPERATOR
# < , >, ==, !=, <=, >=
print(20 != 20)
print(20 == '20')
print(20 == 20.0)
print(0.1+0.2)

a = 100_000_000
print(a)

#LOGICAL OPERATOR: AND OR NOT
print(20==20.0 and 20=='20')
print(20==20.0 or 20=='20')

print(not 9.99 > 10)

#IF STATEMENT
age = int(input("Enter your Age: "))
degree = input("Enter your degree: ")
if age>18:
    if degree=="bachelor":
        print("Eligible for Master Degree")
else:
    print("Not Eligible for Master Degree")

if age<=5:
    print("Ticket Price: 0")
elif (age>5 and age<=10):
    print("Ticket Price: 5")
elif(age>10 and age<=60):
    print("Ticket Price: 15")
elif age>60:
    print("Ticket Price: 10% Consession")
else:
    print("Not Valid Age")


marks = int(input("Enter your Marks: "))
# (marks>40) ? print("Pass") : print("fail")
print("Pass") if (marks>40) else print("Fail")

# FOR LOOP
# for(i=0;i<10;i++){
#     cout<<i
# }
fruits = ["mango", "grapes", "banana", "apple"]
for i in range(0,10,2):
    print(i)

for i in fruits:
    print(i)