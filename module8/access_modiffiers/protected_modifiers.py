class MyClass:
    def __init__(self):
        self._protected_variable = "this a private variable"

    def __protected_method(self):
        print("this is a private method")


my_class = MyClass()

print(my_class.__protected_variable)
print(my_class.__protected_method())