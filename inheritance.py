# class User:
#     def __init__(self,name,age,gender,dob):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.dob=dob
#     def login(self):
#         print("login success")
#     def logout(self):
#         print("logout success")
# class Instagram(User):
#     def post(self):
#         print(f"{self.name} post")
#         print("Got 1k likes")
# id1=Instagram("karthik",18,"male","11 mar 2005")
#
#
#
# class Restaurants:
#     def __init__(self,name,rating,address,item):
#         self.name=name
#         self.rating=rating
#         self.address=address
#         self.item=item
#     def display_menu(self):
#         print("All dishes are non-veg only")
# class Swiggy(User,Restaurants):
#     def display_order(self):
#         print("ordered")
# class Zomato(User,Restaurants):
#     def display_order(self):
#         print("zomato")
# class Customer(Swiggy,Zomato):
#     def order(self):
#         print("Ordering")
# s1=Swiggy("karthik",21,"male","20 mar 2004")
# s1.display_order()
# s1.display_menu()
# s1.logout()
# s1.login()
# s1.display_order()


#
# class User:
#     def order(self):
#         print("ordered biryani")
# class Restaurant(User):
#     def order(self):
#         super().order()
#         print("ordered received")
# class Swiggy(Restaurant):
#     def order(self):
#         super().order()
#         print("Asssigned partner")
#     def order(self):
#
#         print("Order delivered")
# s1=Swiggy()
# s1.order()

# class Animal:
#     def sound(self):
#         print("I'm an animal")
# class Dog(Animal):
#     def sound(self):
#         print("I'm a dog")
#         super().sound()
# a=Animal()
# a.sound()
# dog = Dog()
# dog.sound()


# class A:
#     def display(self):
#         print("A")
# class B(A):
#     def display(self):
#         print("B")
#         super().display()
# class C(B):
#     def display(self):
#         print("C")
#         super().display()
# c1=C()
# c1.display()
# print(C.mro())
#
# class Vehicle:
#     def wheels(self):
#         print("Wheels")
# class Car(Vehicle):
#     def wheels(self):
#         print("Car wheels")
#         super().wheels()
# class Truck(Vehicle):
#     def wheels(self):
#         print("Truck wheels")
#         super().wheels()
# truck = Truck()
# truck.wheels()
# car = Car()
# car.wheels()

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def salary(self):
        return self.base_salary
class Manager(Employee):
    def __init__(self, name, base_salary, incentive):
        super().__init__(name, base_salary)   # call Employee constructor
        self.incentive = incentive
    def salary(self):
        return self.base_salary + self.incentive

emp = Employee("Alice", 50000)
mgr = Manager("Bob", 70000, 10000)

print(emp.salary())
print(mgr.salary())
print(emp.base_salary)




