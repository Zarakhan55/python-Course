class Student:

    def __init__(self, marks):
        self.__marks = marks

    def show_marks(self):
        print("Marks:", self.__marks)


student1 = Student(90)

student1.show_marks()

# --------------------------

class Student:
    def __init__(self,name,mark):
        self. __mark=mark
    def show(self):
        print("mark..")
        