# Hierarchical Inheritance

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showdetails(self):
        print(f"name:{self.name}, age:{self.age}")
    def eat(self):
        print('I can eat')

class Male(Human):
    def __init__(self,name,age,company):
        super().__init__(name,age)
        self.company=company

    def work(self):
        print('I can work')

class Female(Human):
    def __init__(self,name,age,can_dance):
        Human.__init__(self,name,age)
        self.can_dance=can_dance

    def showdetails_F(self):
        Human.showdetails(self)
        print(f"know_dancing:{self.can_dance}")
    def sleep(self):
        print('I can sleep')

female_1=Female('Jiya',20,True)
female_1.showdetails_F()

male_1=Male("Ram",25,'Dell')
print(male_1.company)
