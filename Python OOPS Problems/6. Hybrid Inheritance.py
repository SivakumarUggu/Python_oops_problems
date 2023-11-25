# Hybrid Inheritance
class A:
    def __init__(self,u_name):
        self.name=u_name
    def details(self):
        print(f"u_name: {self.name}")
    def display(self):
        print('I am from class A.')

class B(A):
    def __init__(self,u_name,bot):
        A.__init__(self,u_name)
        self.bot=bot
    def showdetails(self):
         A.details(self)
         print(f'bot: {self.bot}')
    def display(self):
        print('I am from class B.')

class C:
    def show(self):
        print('I am from class C.')

class D(B,C):
    def __init__(self,u_name,bot,dom):
        B.__init__(self,u_name, bot)
        self.dom=dom
    def display(self):
        B.showdetails(self)
        print(f"dom: {self.dom}")
        print('I am from class D.')

d1=D('RGM','Vasi','Dominos')
d1.display()

print(D.mro())   # Method resolution order



