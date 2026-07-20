age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to take exams.")
else:
    print("You are not eligible to take exams.")
    
mark=int(input("Enter your marks:"))
if mark>=90:
    print("You got A+ grade.")
elif mark>=80:
    print("You got A grade.")
elif mark>=70:
    print("You got B grade.")
elif mark>=60:
    print("You got C grade.")
else:
    print("You got F grade.")
    