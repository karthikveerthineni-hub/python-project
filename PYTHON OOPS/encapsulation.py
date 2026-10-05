class A:
    def __init__(self):
        self._x=5
        self.__y=10
    def getx(self):
        if input()=="1234":
            return self._x
        return None
    def setx(self, value):
        if value >27:
            self._x=value
        else:
            print("value of x should be greater than 27")
    @property
    def ac(self):
        return self._x
    @ac.setter
    def ac(self, value):
        self._x=value
    def gety(self):
        return self.__y
    def sety(self, value):
        self.__y=value
        return self.__y
obj=A()
obj.fs=88
print(obj.fs)
print(obj.gety())
# print(obj.getx())
# print(obj.sety(100))

# print(obj._A__y)#name mangling
# print(obj.getx())
# print(obj.gety())
# obj.setx(100)
# print(obj.getx())



# class BankAccount:
#     def __init__(self,name):
#         self.name=name
#         self._balance=0
#         self.__atmpin="1234"
#     def getbalance(self):
#         return self._balance
#     def setpin(self,pin):
#         if input("enter previous atm pin: ")==self.__atmpin:
#             self.__atmpin=pin
#         else:
#             print("pin incorrect")
# class UPI(BankAccount):
#     def sendmoney(self,amount):
#         if self._balance>amount:
#             self._balance=self._balance-amount
#         else:
#             print("insufficient balance")
#     def receivemoney(self,amount):
#         self._balance=self._balance+amount
# b1=BankAccount("madhu")
# print(b1.getbalance())
# upi=UPI("madhu")
# print(upi.getbalance())
# upi.sendmoney(100)
# upi.receivemoney(1000000000000)
# upi.sendmoney(100)
# print(upi.getbalance())
#
# b1.setpin("12345")
# b1.setpin("3456")

# class A:
#     def __init__(self):
#         self._x=5
#         self.__y=10
# a=A()
# print(a._x)
'''Getter and Setter Methods  Getter and
 setter methods are used to read 
and update private data safely.
 1.  Getter method reads private data.
  2.  Setter method updates private data.
   3.  Setter can validate data before updating. 
 4.  This protects the object from invalid values. '''
'''for example'''
# def get_value(self):
#     return self._x
# def set_value(self, value):
#     self._x = value

'''@property  allows a method to behave like an attribute. '''
# @property
# def x(self):
#     return self._x
'''1.  @property  is a clean way to control access to data. 
2.  It allows validation before changing data. 
3.  It supports getter and setter behavior. 
4.  It makes code look simple while still protecting data. '''

class Student:
    def __init__(self, marks):
        self._marks = marks
    @property
    def marks(self):
        return self._marks
    def get(self):
        return self._marks
    def set(self, value):
        self._marks = value
    @marks.setter
    def marks(self, value):
        self._marks = value
student = Student(85)
print(student.marks)
student.marks=56

print(student.marks)
