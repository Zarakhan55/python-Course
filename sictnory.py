# numbers = [2, 3, 2, 4, 3, 2]

# count = {}
# for num in numbers:
#     if num in count:
#         count[num]+=1
#     else:
#        count[num] = 1
# print(count)

# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85
# }
# for key, value in student.items():
#     print(key, ":", value)


# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85
# }

# student["marks"] = 98

# print(student)

# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85
# }
# if "email" in student:
#     print("Email exists")
# else:
#     print("Email not exists")

student = {
    "name": "Zara",
    "age": 22,
    "marks": 85
}
del student["age"]
student["email"]="zarakhan@gmai.com"
print(student)
new=student.keys()
print(new)