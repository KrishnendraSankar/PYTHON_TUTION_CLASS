class Document:
    version = 1.0
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def __str__(self):
        return f'Document({self.name}, {self.type})'
    def __repr__(self):
        return f'Document({self.name}, {self.type})'

d1 = Document("BTECH CSE Syllabus", "PDF")
print(d1)
print(repr(d1))
print(d1.name)
print(d1.type)
print(d1.version)
d2 = Document("", "")
print(d2.version)