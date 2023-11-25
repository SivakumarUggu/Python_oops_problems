#Single Level Inheritance
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eating(self):
        print('eating')

class Dog(Animal):
    def sound(self):
        print('barking')

    def display(self):
        print(self.name,self.age)

dog=Dog('Teddy', 4)
dog.display()
dog.sound()
dog.eating()
