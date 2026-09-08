# text = "hello"
# reverse= ""
# for char in text:
#     reverse=char+reverse
#     print(reverse)
    
# # text = "education"
# count = 0

# for char in text:
#     if char in "aeiou":
#         count=count+1

# print(count)


# text = "programming"

# count = 0

# for char in text:
#     if char in "aeiou":
#         # print("Not consonant")
#     else:
#         count = count + 1

# print("Number of consonants:", count)


# text = "madam"
# reverse = ""

# for char in text:
#     reverse = char + reverse

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# text = "I love learning Python"
# words = text.split()
# result=len(words)
# print(result)



text = "I love programming very much"

words = text.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)