# class Student():
#     pass
# obj=Student()
# print(obj) #we are getting the object address

# class student():
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def display(self):
#         print(f"Student name is {self.name} and age is {self.age} and gender is {self.gender}")
# obj1=student("ravi",21,"male")
# obj2=student("karthi",22,"male")
# obj3=student("srinu",23,"male")
#
# obj1.display()
# obj2.display()
# obj3.display()

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def describe(self):
#         print(self.make, self.model, self.year)
#     def start(self ):
#         print("starting car",self.model)
#     def drive(self):
#         print("driving car",self.make)
# car1 = Car("Ford", "Mustang", "2015")
# car1.describe()
# car1.start()
# car1.drive()

#Changing object variables
# class Car:
#     def __init__(self,speed):
#         self.speed = speed
#     def accelerate(self):
#         self.speed = self.speed + 10
# car1 = Car(100)
# print(car1.speed)
# car1.accelerate()
# print(car1.speed)

# class BankBalance():
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
# balance1 = BankBalance("karthik", 10000)
# print(balance1.owner, balance1.balance)
# balance1.deposit(100)
# print(balance1.balance)
# balance1.withdraw(200)
# print(balance1.balance)

# class Withdraw:
#     def __init__(self, balance):
#         self.balance = balance
#     def draw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"You withdraw ${amount}")
#         else:
#             print("You don't have enough money")
# balance_1 = Withdraw(6000)
# print(balance_1.balance)
# balance_1.draw(4000)
# print(balance_1.balance)
# # balance_1.draw(4000)
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def discount(self, amount):
#         self.price = self.price*amount/100
# price1 = Product("Collage fee", 100)
# print(price1.name,price1.price)
# price1.discount(10)
# print(price1.name,int(price1.price))

#
# class Add:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a*10 + self.b*15
#     def sub(self):
#         if self.a < self.b:
#             return self.a - self.b
#         else:
#            return self.b - self.a
# add1=Add(10,8)
# print(add1.a,add1.b)
# result=add1.add()
# print(result)
# result=add1.sub()
# if result<0:
#     result=result*-1
# print(result)

#
# class Student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#     def is_passed(self):
#         if self.marks > 40:
#             return True
#         else:
#             return False
# student1=Student("James",100)
# print(student1.name,student1.marks)
# print(student1.is_passed())
# student2=Student("karthik",30)
# print(student2.is_passed())

# class MathOps:
#     @staticmethod
#     def add(a, b):
#         return a + b
#     @staticmethod
#     def sub(a, b):
#         return a - b
# add1=MathOps()
# print(add1.add(1,2))
# print(add1.sub(1,2))
# add1=MathOps.add
# sub1=MathOps.sub
# print(add1(1,2))
# print(sub1(1,2))

# class Car:
#     def __init__(self,mileage):
#         self.mileage = mileage
#     wheels = 4
#     def display_specs(self):
#         print(self.mileage)
#         print(self.wheels+2)
#     @classmethod
#     def display_car(cls,new_wheels):
#         cls.new_wheels = new_wheels
#         print(cls.new_wheels)
# o=Car(5)
# o.display_specs()
# o.display_car(5)
#
# class Temperature:
#     celsius = 23.0
#     @staticmethod
#     def to_fahrenheit():
#
#          fahrenheit = Temperature.celsius * 9 / 5 + 32
#          return fahrenheit

    # def to_fahrenheit(self):
    #     self.fahrenheit = Temperature.celsius * 9 / 5 + 32
    #     return self.fahrenheit

    # def to_fahrenheit(fahrenheit):
    #     fahrenheit = Temperature.celsius * 9 / 5 + 32
    #     return fahrenheit

#     def show_conversion(self):
#         print(self.celsius)
#         print(self.to_fahrenheit())
# obj = Temperature()
# obj.show_conversion()

# class Book:
#     total_books = 0
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.total_books += 1


    # @classmethod
    # def from_string(cls,book_str):
    #     title,author = book_str.split('-',1)
    #     return cls(title,author)
#     @staticmethod
#     def is_valid(title):
#         return len(title) >=3
# obj=Book("python class","karthi")
# print(obj.title,obj.author)
# obj.is_valid("python class")
# print(obj.total_books)

#
# class Employee:
#     bonus_rate = 0.1 # class variable
#     def __init__(self,name,base_salary): #instance attributes
#         self.name = name
#         self.base_salary = base_salary
#     def final_salary(self):
#         return self.base_salary+(self.base_salary * self.bonus_rate)
#     @classmethod
#     def update_bonus(cls,new_rate):
#         cls.bonus_rate = new_rate
#     @staticmethod
#     def is_valid_salary(salary):
#         if salary >0:
#             return f"The salary is  {salary},so it is valid."
#         else:
#             return False
# obj1 = Employee("karthik",59000)
# print(obj1.bonus_rate)
# print(obj1.final_salary())
# Employee.update_bonus(5)
# print(obj1.final_salary())
# s=obj1.is_valid_salary(obj1.final_salary())
# print(s)

# class Course:
#     total_students = 0
#     def __init__(self, student_name):
#         self.student_name = student_name
#         Course.total_students += 1
#     def enroll(self):
#         self.total_students += 1
#     @classmethod
#     def show_total(cls):
#         print(f'Total students: {cls.total_students}')
#     @staticmethod
#     def is_eligible(age):
#         if age >= 18:
#             return True
#         else:
#             return False
# student=Course("karthik")
# student.enroll()
# student.show_total()
# print(student.is_eligible(19))


# class BankAccount:
#     bank_name = 'SBI'
#     def __init__(self,holder_name,balance):
#         self.holder_name = holder_name
#         self.balance = balance
#     def deposit(self,amount):
#         self.amount = amount
#         return self.amount+self.balance
#     @classmethod
#     def change_bank_name(cls,bank_name):
#         cls.bank_name = bank_name
#     @staticmethod
#     def validate_bank_amount(amount):
#         if amount <=0:
#             return False
#         else:
#             return True
# s=BankAccount("karthik",10000)
# k=s.deposit(100)
# print(k)
# print(s.balance)

# class Student():
#     passing_marks = 40
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def result(self):
#         if self.marks > Student.passing_marks:
#             print("You are passed")
#         else:
#             print("You are failed")
#     @classmethod
#     def update_passing_marks(cls,new_marks):
#         Student.passing_marks = new_marks
#     @staticmethod
#     def grade_category(marks):
#         if marks >= 90:
#             return "A"
#         elif marks >= 80:
#             return "B"
#         elif marks >= 70:
#             return "C"
#         else:
#             return "D"
# student = Student("John", 100)
# student.result()
# student.update_passing_marks(50)
# s=student.grade_category(90)
# print(s)
#
# class Student():
#     total_students = 0
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         Student.total_students += 1
#     passing_marks=40
#     def passing(self):
#         if self.marks>=Student.passing_marks:
#             return "pass"
#         else:
#             return "fail"
#     @classmethod
#     def increment_marks(cls,percentage):
#         cls.passing_marks = cls.passing_marks+cls.passing_marks*percentage
#     @staticmethod
#     def display_scores(marks):
#         if marks>=100:
#             return "grade a"
#         elif marks>=90:
#             return "grade b"
#         elif marks>=80:
#             return "grade c"
#         elif marks>=70:
#             return "grade d"
#         elif marks>=60:
#             return "grade e"
#         else:
#             return "grade f"
# student1 = Student("srinu", 50)
# student2 = Student("karthik", 30)
# s=student1.passing()
# print(s)
# k=student2.passing()
# print(k)
# student1.increment_marks(1)
# print(student1.marks)
# print(Student.passing_marks)
# z=student1.passing()
# print(z)

# class Product:
#     total_products = 0
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.total_products += 1
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     base_tax_rate = 10
#     @classmethod
#     def show_total_products(cls):
#         return cls.total_products
#
#     def final_price(self):
#         return self.price + Product.base_tax_rate
#
#     def change_tax(self, new_tax):
#         self.price += new_tax * Product.base_tax_rate
#     def validate_price(self):
#         if self.price > 0:
#             return "realistic"
#         else:
#             return "not realistic"
# product_1 = Product("Milk", 100)
# print(product_1.final_price())
# product_2 = Product("Milk", 200)
# print(product_2.final_price())
#
#
# class Employee:
#     minimum_experience = 3
#
#     def __init__(self, name, salary, experience, department):
#         self.name = name
#         self.salary = salary
#         self.experience = experience
#         self.department = department
#     def eligibility(self):
#         if self.experience < Employee.minimum_experience:
#             return "Not Eligible for promotion"
#         else:
#             return "Eligible for promotion"
#     @classmethod
#     def update_promotion(cls, promotion_experience):
#         cls.minimum_experience = promotion_experience
#     @staticmethod
#     def vaild_department(department):
#         departments = ["HR","Tech","Admin"]
#         if department in departments:
#             return department
#         else:
#             return False
# employee = Employee("karthik", 20000, 6, "Tech")
# print(employee.eligibility())
# print(employee.vaild_department(employee.department))
# employee.update_promotion(5)
# print(employee.eligibility())





















