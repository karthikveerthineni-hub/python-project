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

# class Bank:
#     def __init__(self, accno, name, pin, balance=0):
#         self.accno = accno
#         self.name = name
#         self.pin = pin
#         self.balance = balance
#     def __add__(self, amount):
#         self.balance += amount
#         print(f"{self.balance} is deposited to bank")
#     def validate_pin(self, entered_pin):
#         return self.pin == entered_pin
#     def __sub__(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"{amount} is withdraw from bank")
#             print(f"Total balance:{self.balance}")
#         else:
#             print("Insufficient balance!")
#     def __call__(self):
#         print(f"Account No: {self.accno}, Name: {self.name}, Balance: {self.balance}")
#     def __gt__(self, other):
#         return self.balance > other.balance
#     def __repr__(self):
#         return f"Account No: {self.accno}, Name: {self.name}, Balance: {self.balance}"
# b1 = Bank(101, "Karthik", 1234)
# b2 = Bank(102, "Naveen", 5678)
# b1 + 30000
# if b1.validate_pin(1234):
#     b1 - 25000
# b1()
# l=[b1,b2]
# print(*l)
# print(b1 > b2)

'''Question 1: Bank Account Operations
Create a class BankAccount with:
•	attributes: account_holder, balance
•	instance method: deposit(amount)
•	instance method: withdraw(amount)
Implement these magic methods:
•	__str__() → display account details
•	__add__() → add balances of two accounts
•	__sub__() → subtract balances
•	__eq__() → compare if two accounts have same balance
•	__lt__() → check which account has lower balance
•	__getattribute__() → print a message whenever an attribute is accessed
•	__setattr__() → prevent setting negative balance
Demonstrate creating two accounts and using all operations.'''
#
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         return self.balance + amount
#     def withdraw(self, amount):
#         if self.balance>=amount:
#             return self.balance-amount
#         else:
#             print("You don't have enough money to withdraw")
#     def __str__(self):
#         return f'Account holder name:{self.account_holder},Balance: {self.balance}'
#     def __add__(self, other):
#         return self.balance + other.balance
#     def __sub__(self, other):
#         return self.balance - other.balance
#     def __eq__(self, other):
#         return self.balance == other.balance
#     def __lt__(self, other):
#         return self.balance < other.balance
#
# b1=BankAccount("John", 30000)
# print(b1)
# b2=BankAccount("Bob", 20000)
# print(b2)
#
# print(b1+b2)
# print(b1-b2)
# print(b1.deposit(10000))
# print(b1.withdraw(10000))
#
#
# '''Question 2: Product Price Comparison
# Create a class Product with:
# •	attributes: name, price, quantity
# •	method: total_price()
# Implement:
# •	__str__()
# •	__add__() → add total prices of two products
# •	__mul__() → multiply product price by a number
# •	__gt__() → compare which product has greater total value
# •	__eq__() → compare prices
# •	__getattr__() → return "Attribute not found" for missing attributes
# •	__setattr__() → do not allow price less than 0 '''
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_price(self):
#         return self.price * self.quantity
#     def __str__(self):
#         return f"name:{self.name}--price:{self.price}--quantity: {self.quantity}"
#     def __add__(self, other):
#         return self.total_price() + other.total_price()
#     def __mul__(self, other):
#         return self.total_price() * other.total_price()
#     def __gt__(self, other):
#         return self.total_price() > other.total_price()
#     def __eq__(self, other):
#         return self.total_price() == other.total_price()
#     def __repr__(self):
#         return f"name:{self.name}--price:{self.price}--quantity: {self.quantity}"
#     def __getattr__(self, name):
#         return f"Attribute not found: {name}"
# p1=Product("F1car",10000000,3)
# p2=Product("TataNexon",1000000,2)
# # print(p1.name, p1.price, p1.quantity)
# print(p1)
# print(p2)
# l=[p1,p2]
# print(l)
# print(p1.total_price())
# print(p1.color)
# print(p1+p2)

# Question 3: Student Marks
# Create a class Student with:
# •	attributes: name, marks
# •	method: grade()
# Implement:
# •	__str__()
# •	__add__() → add marks of two students
# •	__truediv__() → divide marks by a number
# •	__ge__() → check if one student scored greater than or equal to another
# •	__lt__() → check if one student scored less
# •	__getattribute__() → track attribute access
# •	__setattr__() → marks must be between 0 and 100

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
    def __str__(self):
        return f"name:{self.name}--marks:{self.marks}"
    def __add__(self, other):
        return self.marks + other.marks
    def __truediv__(self, other):
        return self.marks / other
    def __ge__(self, other):
        if self.marks >= other.marks:
            return f"{self.name} is greater than {self.marks}"
        else:
            return f"{self.name} is less than {self.marks}"
    def __lt__(self, other):
        if self.marks < other.marks:
            return f"{self.name} is less than {self.marks}"

        else:
            return f"{self.name} is greater than {self.marks}"
s1=Student("karthik",80)
print(s1)
s2=Student("rakesh",90)
print(s2)
print(s1>=s2)
print(s1<s2)