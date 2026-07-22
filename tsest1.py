name = input("Enter your name: ")
print(name)

sub1 = float(input("Enter your English marks: "))
sub2 = float(input("Enter your Math marks: "))
sub3 = float(input("Enter your Chemistry marks: "))

print("Your English marks:",sub1)
print("Your Math marks:",sub2)
print("Your Chemistry marks:",sub3)

total = sub1 + sub2 + sub3
average = total / 3

print("Your name is:", name)
print("Your total number is:", total)
print("Your average is:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

student = {
    "Name": name,
    "English": sub1,
    "Math": sub2,
    "Chemistry": sub3,
    "Total Number": total,
    "Average": average,
    "Grade": grade
}

print("\nStudent Dictionary:")
print(student)