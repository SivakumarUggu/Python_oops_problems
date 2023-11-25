# Multi Level Inheritance

class Employer:
    def display(self):
        print("Hello, I am Your Employer")

class Manager(Employer):
    def work(self):
        print('Work on this')

class Programmer(Manager):
    def progress(self):
        print('Work is finished')

prog=Programmer()

prog.display()
prog.work()
prog.progress()