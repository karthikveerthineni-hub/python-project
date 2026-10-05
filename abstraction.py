# from abc import ABC, abstractmethod
# class Abstraction(ABC):
#     @abstractmethod
#     def car(self):
#         pass
# class Ferrari(Abstraction):
#     def car(self):
#         return "Ferrari"
# ferrari = Ferrari()
# print(ferrari.car())
#
# from abc import ABC, abstractmethod
# class Product(ABC):
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     @abstractmethod
#     def order(self):
#         print("order conform")
#     @abstractmethod
#     def delivered(self):
#         print("delivered")
# print(Product.__abstractmethods__)
# class Electronics(Product):
#     @abstractmethod
#     def eletronics(self):
#         print("eletronics")
# class Iphone(Electronics):
#     def order(self):
#         print("order conform")
#     def delivered(self):
#         print("delivered")
#     def eletronics(self):
#         print("eletronics")
# print(Iphone.__abstractmethods__)
# class Poco(Electronics):
#     def order(self):
#         print("order conform")
#     def delivered(self):
#         print("delivered")
#     def eletronics(self):
#         print("eletronics")
# c1=Iphone("laptop",100)
# c1.delivered()
# c1.order()
# c1.eletronics()
# c2=Poco("laptop",200)
# c2.delivered()
# c2.order()
# c2.eletronics()
# import math
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return 2*self.length*self.width
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return math.pi*self.radius**2
#     def perimeter(self):
#         return 2*math.pi*self.radius
# c1=Rectangle(12,5)
# print(c1.area())
# print(c1.perimeter())
# c2=Circle(5)
# print(c2.area())
# print(c2.perimeter())



# from abc import ABC, abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,amount):
#         pass
# class Upipayment(PaymentGateway):
#     def authenticate(self):
#         print("authenticate")
#     def pay(self,amount):
#         print("pay")
#     def refund(self,amount):
#         print("refund")
# class Cardpayment(PaymentGateway):
#     def authenticate(self):
#         print("authenticate")
#     def pay(self,amount):
#         print("pay")
#     def refund(self,amount):
#         print("refund")
# class NetBanking(PaymentGateway):
#     def authenticate(self):
#         print("authenticate")
#     def pay(self,amount):
#         print("pay")
#     def refund(self,amount):
#         print("refund")
# def make_payment_gateway(payment_gateway,amount):
#     payment_gateway.authenticate() ***creating a method to access sub class methods of the classes
#     payment_gateway.pay(amount)
#     payment_gateway.refund(amount)
# U=Upipayment()
# N=NetBanking()
# C=Cardpayment()
# make_payment_gateway(U,100)
# make_payment_gateway(N,200)
# make_payment_gateway(C,300)

#
# '''13. Create: • Abstract class VehicleControl with methods
#  accelerate(),
#  brake(), steer() • Implement CarControl, BikeControl,
# TruckControl Demonstrate calling each through a
# single interface. '''
# from abc import ABC, abstractmethod
# class VehicleControl(ABC):
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# class CarControl(VehicleControl):
#     def accelerate(self):
#         return "car is moving"
#     def brake(self):
#         return "car is stopped"
#     def steer(self):
#         return "car is driving"
# class BikeControl(VehicleControl):
#     def accelerate(self):
#         return "bike is moving"
#     def brake(self):
#         return "bike is stopped"
#     def steer(self):
#         return "bike is driving"
# class TruckControl(VehicleControl):
#     def accelerate(self):
#         return "truck is moving"
#     def brake(self):
#         return "truck is stopped"
#     def steer(self):
#         return "truck is driving"
# def control(VehicleControl):
#     print(VehicleControl.accelerate())
#     print(VehicleControl.brake())
#     print(VehicleControl.steer())
#
# # print("------------")
# # control(CarControl())
# # print("------------")
# # control(BikeControl())
# # print("------------")
# # control(TruckControl())
# vechicle =[CarControl(),BikeControl(),TruckControl()]
# for v in vechicle:
#     print("------------")
#     control(v)

'''14. Create an abstract class DatabaseDriver with:
 • connect() • execute(query) • close() 
 Implement concrete drivers: • MySQLDriver • PostgresDriver •
  SQLiteDriver Show how abstraction 
helps switch databases without rewriting main code. '''

# from abc import ABC, abstractmethod
# from idlelib import query
#
#
# class DatabaseDriver(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def execute(self, query):
#         pass
#     @abstractmethod
#     def close(self):
#         pass
# class SQLiteDriver(DatabaseDriver):
#     def connect(self):
#         print("connecting to sqlite database")
#     def execute(self, query):
#         print("executing query")
#         print("---query---")
#         print(query)
#
#     def close(self):
#         print("closing sqlite database")
# class MySQLDriver(DatabaseDriver):
#     def connect(self):
#         print("connecting to mysql database")
#     def execute(self, query):
#         print("executing query")
#     def close(self):
#         print("closing mysql database")
# class PostgresDriver(DatabaseDriver):
#     def connect(self):
#         print("connecting to postgres database")
#     def execute(self, query):
#         print("executing query")
#         print(query)
#     def close(self):
#         print("closing postgres database")
# def server(DatabaseDriver,query):
#     DatabaseDriver.connect()
#     DatabaseDriver.execute(query)
#     DatabaseDriver.close()
# server(SQLiteDriver(),"select * from sqlite_master where type='table'")
#

''' Create an abstract class MLModel with:
 • train(data) • predict(x) • evaluate(test_set)
 Implement models: • LinearRegressionModel- 
some different logic • DecisionTreeModel –
 some logic Show how a
 generic training loop works for any 
model without caring about details. '''

from abc import ABC, abstractmethod


# Abstract class
class MLModel(ABC):

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass

    @abstractmethod
    def evaluate(self, test_set):
        pass
class LinearRegressionModel(MLModel):
    def train(self, data):
        print("Training Linear Regression model...")
        self.coefficient = 2
        self.intercept = 1
    def predict(self, x):
        return self.coefficient * x + self.intercept

    def evaluate(self, test_set):
        print("Evaluating Linear Regression model...")
        predictions = [self.predict(x) for x in test_set]
        print("Predictions:", predictions)
# Decision Tree implementation
class DecisionTreeModel(MLModel):
    def train(self, data):
        print("Training Decision Tree model...")
        self.threshold = 5

    def predict(self, x):
        if x > self.threshold:
            return "Class A"
        else:
            return "Class B"

    def evaluate(self, test_set):
        print("Evaluating Decision Tree model...")
        predictions = [self.predict(x) for x in test_set]
        print("Predictions:", predictions)


# Generic training loop
def training_loop(model, train_data, test_data):
    print("\n--- Training Process ---")
    model.train(train_data)
    print("\n--- Prediction ---")
    for x in test_data:
        print("Input:", x, "Prediction:", model.predict(x))
    print("\n--- Evaluation ---")
    model.evaluate(test_data)


# Create different models
linear_model = LinearRegressionModel()
tree_model = DecisionTreeModel()


# Same training loop works for both models
training_loop(
    linear_model,
    [1, 2, 3, 4, 5],
    [2, 6, 8]
)

training_loop(
    tree_model,
    [1, 2, 3, 4, 5],
    [2, 6, 8]
)


