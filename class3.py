x = 10
i = 0
while i<x: #condition 
    print(i) #statement
    i = i+2 # increment / decrement

print("====================BREAK===========================")
for j in range(0,6,2): # outer loop
    for i in range(0,10,2): # inner loop
        if(i > 5):
            break
        print(f"({j},{i})")


print("====================BREAK USING WHILE===========================") 

l = 0
while l<6:
    k = 0
    while k<10: #condition 
        if(k > 5):
            break
        print(f"({l},{k})")
        k = k+2 # increment / decrement
    l = l+2


print("====================CONTINUE===========================") 
for i in range(0,10): # inner loop
        if(i % 2 != 0):
            continue
        print(i)

print("====================FUNCTIONS===========================") 
def add(q,w):
    e = q+w
    return e
result = add(2,5)
print(result)

def calculator():
    num1 = int(input("Enter the number"))
    num2 = int(input("Enter the number"))
    ch = input("Enter any operator +,-,/,* ")
    result = 0
    if ch =='+':
        result = num1 + num2
        
    elif ch =='-':
        result = num1 - num2
        
    elif ch == '/':
        result = num1 / num2
        
    elif ch =='*':
        result = num1 * num2
    
  
    print (num1,num2,ch,result)