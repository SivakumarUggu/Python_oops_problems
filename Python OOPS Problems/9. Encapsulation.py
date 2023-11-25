class Student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        # self.__age=age
        # return self.__age
        if age>35:
            print("Invalid age given. age must be less than 35")
        else:
            self.__age=age

s1=Student("rahul", '21A', 30)
print(s1.get_age())
s1.set_age(31)
print(s1.get_age())

# print(s1.name)
# print(s1._rollno)
# print(s1.__age)
