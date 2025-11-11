# names = ["shpat", "bob", "ensar", "gent"]
#
# for name in names:
#     print(name)
from moduli3.sets import student_score

# sentence = "hello world"
#
# for character in sentence:
#     if character.isalpha():
#         print (character)
#
# numbers = [12, 45, 53, 86, 98, 1, 2]
#
# maximum = numbers [0]
#
# for num in numbers:
#     if num > maximum:
#         maximum = num
#     print("the maximum number value in the list is: ", maximum)

# count = 1
#
# while count <= 5:
#     print("iteraction: ", count)
#     count += 1

# numbers = [1, 2, 3, 4, 5]
# target = 4
#
# for number in numbers:
#     print (number)
#     if number == target:
#         print("target found")
#         break

# scores = [68, 42, 65, 78]
# total = 0
# count = 0
#
# for score in scores:
#     if score < 50:
#         continue
#         total += score
#         count += 1
#
# average = total / count if count > 0 else 0
#
# print("average score above 50: ", average)

while True:

    user_input = input("enter a positive number: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break

    print("ivalid input. try again: ")
print("you entered a valid positive number")







