# my_set = {1, 2, 3}
# my_set = set()
# my_set = set([4, 5, 6])
#
# print(my_set)

#
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# union_result_method = set1.union(set2)
# print("Union: ", union_result_method)
#
# union = set1 | set2
# print("Union method: ", union)
#
# intersection = set1 & set2
# print("intersection method: ", intersection)
#
# difference = set1 - set2
# print("difference method: ", difference)
#
# symmetrical_difference = set1 ^ set2
# print("symmetrical_difference method: ", symmetrical_difference)

#Set methods

# my_set = {1, 2, 3}
#
# my_set.add(4)
# my_set.remove(3)
# my_set.discard(1)
# my_set.clear()
#
# print (my_set)
#
# set_length = len(my_set)
# print("lenght of set: ", set_length)

# Using sets - removing duplicates

# my_list = [1, 2, 2,2, 3, 3, 3, 4, 5]
#
# unique_set = set(my_list)
#
# unique_list = list (unique_set)
#
# print(unique_list)

# IN and NOT IN

# loyalty_members = {"shpat", "gent", "ensar"}
# customer = "gent"
#
# is_member = customer in loyalty_members
# is_member = customer not in loyalty_members
#
# print(is_member)

# age = 18
#
# if age >= 18:
#     print("you can vote")
# else:
#     print("you cannot vote")


# temp = 18
#
# if temp >= 30:
#     print("its a hot day")
# elif 20 <= temp <= 30:
#     print("its a good day")
# else:
#     print("it a cold day")


student_gpa = 4.5
student_score = 75

if student_gpa >= 3.5:
  if 50 >= student_score <= 65:
    print(f"students with gpa {student_gpa} and test score of {student_score} may be eligitable for a partial scholarship")
  elif student_score > 65:
    print(f"students with gpa {student_gpa} and test score of {student_score} may be eligitable for a partial scholarship")
  else:
      print(
          f"students with gpa {student_gpa} and test score of {student_score} is not eligitable for a scholarship")


else:
    print(f"students with gpa {student_gpa} and test score of {student_score} is not eligitable for a scholarship")
