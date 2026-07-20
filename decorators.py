# def decorator(func):
#     def wrapper(a,b):
#         print("Before Function execution")
#         print(func.__name__)
#         func(a,b)
#         print("After Function execution")
#     return wrapper
# @decorator
# def greet(a,b):
#     print(a+b)
# print(greet.__name__)
# greet(10,20)
from email import message


# def login(func):
#     def inner():
#         un=input("Enter your username: ")
#         pw=input("Enter your password: ")
#         if un=="karthikveerthineni" and pw=="karthik":
#             return func()
#         else:
#             print("Wrong username or password")
#     return inner
# @login
# def loggedin():
#     return "welcome your account is logged in"
# print(loggedin())

# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end-start:.4f}s")
#         return result
#     return wrapper
#
# @timer
# def compute():
#     sum([i for i in range(10000)])
#
# compute()

# def valid(func):
#     uns=[]
#     special_char=['@','#','$','%','^','&','*']
#     def inner(us,pw):
#         if 8<= len >=15:
#             k=list(filter(lambda x:x in special_char,pw))
#             n=list(filter(lambda x:x.isdigit,pw))
#             up=list(filter(lambda x:x.isupper,pw))

# import functools
# def ann(func):
#     @functools.wraps(func)
#     def inner(x,y):
#
#         print(x,y)
#         return func(x,y)
#     return inner
# @ann
# def fun(a:int, b:int) -> int:
#     return a+b
# print(fun(3,4))
# print(fun.__doc__)
# print(fun.__annotations__)
# print(fun.__name__)

# def outer():
#     message = 'I am outer'
#     def inner():
#         print(message)
#     inner()
# outer()
#
# def greet():
#     print("Hello World")
# greet()


# def greet():
#     def inner():
#         print("Hello")
#     return inner
# k=greet()
# k()

def my_decorator(func):
    def wrapper():
        print("Before decoration")
        func()
        print("After decoration")
    return wrapper

def my_function():
    print("decorated")
my_function=my_decorator(my_function)
my_function()





