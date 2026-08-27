class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

    def show_student(self):
        print("Student:", self.name)
        print("Age:", self.age)
        print("Marks:", self.__marks)


class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(self.name, "is teaching", self.subject)


# Aggregation
class School:

    def __init__(self, student, teacher):
        self.student = student
        self.teacher = teacher

    def show_school(self):
        print("----- School Information -----")

        self.student.show_student()

        print("Teacher:", self.teacher.name)
        print("Subject:", self.teacher.subject)

        self.teacher.teach()


# Objects
s1 = Student("Zara", 22, 85)
t1 = Teacher("Ali", "Python")

# School receives existing objects
school = School(s1, t1)

school.show_school()

print("----------------")

# Using setter
s1.marks = 90

print("New Marks:", s1.marks)