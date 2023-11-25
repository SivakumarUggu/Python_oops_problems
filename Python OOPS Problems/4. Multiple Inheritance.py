# Multiple Inheritance

class Land_Animal:
    def Living(self):
        print('This animal lives on land.')

class Water_Animal:
    def Staying(self):
        print('This animal lives in water.')

class Frog(Land_Animal, Water_Animal):
    pass

F=Frog()
F.Living()
F.Staying()


