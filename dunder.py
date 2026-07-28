# class Bank:
#     def __init__(self,name,account):
#         self.name=name
#         self.account=account
#         self.balance=0
#     def __hash__(self):
#         return hash(self.account)
#     def __eq__(self,other):
#         return self.account == other.account and self.name == other.name
#
# b1=Bank("Bank",1)
# b2=Bank("Bank",2)
# k={b1,b2}
# print(b1==b2)
#
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __gt__(self, other):
#         return self.age > other.age and len(self.name) > len(other.name)
#     def __lt__(self, other):
#         return self.age < other.age
#     def __ge__(self, other):
#         return self.age >= other.age
#     def __le__(self, other):
#         return self.age <= other.age
#     def __eq__(self, other):
#         return self.age == other.age
#     def __ne__(self, other):
#         return self.age != other.age
# s1=Student("John",25)
# s2=Student("karthik",22)
# print("---students details---")
# print(s1.name,s1.age)
# print(s2.name,s2.age)
# print(s1>s2)
# print(s1>=s2)
# print(s1<=s2)
# print(s1==s2)
# print(s1!=s2)

class Bank:
    def __init__(self, accno, name, pin, balance=0):
        self.accno = accno
        self.name = name
        self.pin = pin
        self.balance = balance
    def __add__(self, amount):
        self.balance += amount
        print(f"{self.balance} is deposited to bank")
    def validate_pin(self, entered_pin):
        return self.pin == entered_pin
    def __sub__(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} is withdraw from bank")
            print(f"Total balance:{self.balance}")
        else:
            print("Insufficient balance!")
    def __call__(self):
        print(f"Account No: {self.accno}, Name: {self.name}, Balance: {self.balance}")
    def __gt__(self, other):
        return self.balance > other.balance
    def __repr__(self):
        return f"Account No: {self.accno}, Name: {self.name}, Balance: {self.balance}"
b1 = Bank(101, "Karthik", 1234)
b2 = Bank(102, "Naveen", 5678)
b1 + 30000
if b1.validate_pin(1234):
    b1 - 25000
b1()
l=[b1,b2]
print(*l)
print(b1 > b2)












