class Student:
    def __init__(self,name,rollno):
        self.name=name         #Public Instance Variable
        self._rollno=rollno    #Protected Instance Variable

    def display(self):
        print(f"Hi, myself: {self.name} and rollno is: {self._rollno}.")

class Branch(Student):
    pass

def Showdata():
  b1=Branch('nisha',22)
  print(b1._rollno)

  s1=Student("rock", 30)
  s1.display()

Showdata()