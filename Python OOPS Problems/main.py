from Abstract_Class import Vehicle

class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color

    def start(self):
        print("Bike starts with kick.")

class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)

    def start(self):
        print("Scooty starts with Self.")

class Car(Vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.x=6
    def start(self):
        print("Car starts with Key.")