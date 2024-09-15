class Person:
    def __init__(self, height):
        self.height = height
    def greet(self):
        return f"Hi, My height is {self.height}"

class Student(Person):
    def __init__(self,name, age, h):
        self.personName = name
        self.personAge = age
        super().__init__(height=h)
    def greet(self):
        return f"Hi, My name is {self.personName}. I am {self.personAge} years old. My height is {self.height} ft. I am a student."


s1 = Student("samapti", "21", 5)
print(s1.greet())