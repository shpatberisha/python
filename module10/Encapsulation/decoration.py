class Studenti:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name


    @property
    def age(self):
        return slef.__age

    @age.setter
    def age(self,age):
        self.__age=age

student1=Studenti("Daris",15)

print("Name:",student1.name)
student1.name="Blin"
print("Name:",student1.name)
