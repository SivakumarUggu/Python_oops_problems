class Student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age

    def display(self):
        print(f"Myself: {self.name} of age: {self.__age} with rollno: {self._rollno}.")

class Branch(Student):
    pass

s1=Student('Krish','11091A', 20)
s1.display()
#print(s1.__age)