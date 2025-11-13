# def greet():
#   print("hello world")
#
# greet()
#
# def greet_person(name):
#     print("hello",name)
#
# greet_person("daris")
# greet_person("gent")


#
# def greet(name):
#     message=f"hello,{name}"
#     print(message)
#
# greet("alice")
# # print(message)

# greeting="hello"
#
# def greet(name):
#     message=f"{greeting},{name}"
#     print(message)
#
# greet("bob")
# print(greeting )

greeting="hello"

#
# def greet():
#     global greeting
#     greeting="goodbye"
#     name="alice"
#
#     message=f"{greeting},{name}"nju
#
#     print(message)
#
# greet()
# print(greeting)

def greet_person(name,greeting="hello"):
    message=f"{greeting},{name}"
    return message

print(greet_person("alice"))
print(greet_person("bob","hi"))





