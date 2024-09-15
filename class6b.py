class Person:
    def __init__(self, name, age):
        self.personName = name
        self.personAge = age
    def greet(self):
        return f"Hi, My name is {self.personName}. I am {self.personAge} years old."

p1 = Person("samapti", "21")
p2 = Person("Tushar", 31)
print(p1.personName)
print(p1.personAge)
print(p1.greet())