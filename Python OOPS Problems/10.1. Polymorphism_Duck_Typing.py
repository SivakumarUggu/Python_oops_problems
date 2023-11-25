class Duck:
    def swim(self):
        print("I am a duck and i can swim.")
    def speaks(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a dog and i can swim")
    def speaks(self):
        print("Woof Woof")

class Person:
    def speaks(self):
        print("Blah Blah")

def display(obj):
    obj.swim()
    obj.speaks()
    print("Information Displayed.")

d=Duck()
dog=Dog()
p=Person()

display(d)
display(dog)
display(p)