# class Demo:
#     def add(self,*args): #Python does not support method overloading but we can achieve
#                          # this with default arg(def add(self,a,b,c=0): or using *args.
#         total=0
#         for i in args:
#             total=total+i
#         return total
#
#
# d=Demo()
# print(d.add(1,2))
# print(d.add(1,2,3))
# print(d.add(3,4,5,3,10,5))

#Method Overriding

class Father:
    def sleep(self):
        print("He sleeps from 10PM to 6AM.")
    def eat(self):
        print("He is vegiterian")

class Son(Father):
    def sleep(self):
        print("He sleeps from 2PM to 10AM.")
        super().sleep()
s=Son()
s.sleep()
