# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85
# }
# total = 0
# for value in student.values():
#     if isinstance(value, (int, float)):
#         total += value
#         print(total)


# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85,
#     "city": "Karachi"
# }
# count = 0
# for value in student.values():
#     if isinstance(value ,(int,float)):
#         count+=1
#         print(count)


# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85,
#     "city": "Karachi"
# }
# count = 0
# for value in student.values():
#     if isinstance(value ,(int,float)):
#         count+=1
#         print(count)

# student = {
#     "name": "Zara",
#     "age": 22,
#     "marks": 85
# }
# total = 0
# count = 0
# for value in student.values():
#     if isinstance(value ,(int,float)):
#         total+=value
#         count+=1
# aveareg=total/count
# print(aveareg)











student = {
    "name": "Zara",
    "age": 22,
    "marks": 85,
    "city": "Karachi"
}
highest=0
for value in student.values():
    if isinstance(value,(int,float)):
           if value > highest:
            highest = value
            print(highest)
