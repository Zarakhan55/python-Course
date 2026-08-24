class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
s1=Student("zara")
print(s1)        

class Library:
    def __init__(self,Title,author):
        self.Title=Title
        self.author=author
    def __str__(self):
        return self.Title
b1=Library("chemistry","zara")
print(b1) 