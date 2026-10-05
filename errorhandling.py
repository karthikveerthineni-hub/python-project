from logging import exception

# a=int(input())
# b=int(input())
# try:
#     print("success")
#     print(a//b)
# except Exception as e:
#     print(e)

# try:
#     a=10
#     b=0
#     print(a//b)
# except ZeroDivisionError:
#     print("division by zero")
# try:
#     c=100
#     d='12'
#     print(c//d)
# except ValueError:
#     print("ValueError")
# except TypeError:
#     print("TypeError")
# except Exception as e:
#     print(e)
#     print("exception")
# else:
#     print("else block exception")
# finally:
#     print(a)
#
# try:
#     number = int(input("Enter number: "))
#     result = 100 / number
#
# except ValueError:
#     print("Please enter a number")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#
# else:
#     print("Result:", result)
#
# finally:
#     print("Execution completed")

# try:
#     number = int(input("Enter number: "))
#     result = 100 / number
#
# except (ValueError, ZeroDivisionError) as e:
#     print("Error:", e)

#
# class BankAccount:
#
#     def __init__(self, balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#
#         if amount > self.balance:
#             raise ValueError("Insufficient balance")
#
#         self.balance -= amount
#         print("Withdrawal successful")
# bank_account = BankAccount(100)
# bank_account.withdraw(100)
# try:
#     bank_account.withdraw(2000)
# except ValueError as e:
#     print("Transcation failed : ",e)
#
# nl=[[0,1,1,0],
#     [0,1,1,0],
#     [0,1,1,0],
#     [0,1,1,0]]
#
# c=0
# for i in range(0,len(nl)):
#     for j in range(0,len(nl[i])):
#         if nl[i][j] == 1:
#             if nl[i][j-1] == 0 or j==0:
#                 c=c+1
#             if nl[i-1][j] == 0 or i==0:
#                 c=c+1
#             try:
#                 if nl[i+1][j] == 0:
#                     c=c+1
#             except:
#                 c=c+1
#             try:
#                 if nl[i][j+1] == 0:
#                     c=c+1
#             except:
#                 c=c+1
# print(c)



# nl=[[0,1,1,0],
#     [0,1,1,0],
#     [0,1,1,0],
#     [1,1,1,1]]
# print(nl[-1][0])
#
# import copy
# a=[[1,2],[3,4],[5,6]]
# # c=copy.copy(a) #shallowcopy
# d=copy.deepcopy(a)
# d[0][0]=100
# # c[0][0]=100
# # print(c)
# print(d)
# print(a)

#
# class Person:
#     def __init__(self, age):
#         self.age = age
#     def ages(self):
#         if self.age < 0:
#             raise ValueError("You can't do that")
#         else:
#             return self.age
# obj=Person(5)
# print(obj.ages())
# obj1=Person(-1)
# print(obj1.ages())
#
# def fun(obj):
#     c=0
#     try:
#         for _ in obj:
#             c+=1
#         return c
#     except:
#         raise TypeError("typeerror")
# print(fun("hello"))
# try:
#     print(fun(122))
# except:
#     print(fun("kd"))
#
# class Marks:
#     def __init__(self, mark):
#         self.mark = mark
#     def set_marks(self):
#         if self.mark<=0 or self.mark>=100:
#             raise ValueError("Marks cannot be less than 100")
#         else:
#             return self.mark
# obj=Marks(100)
# print(obj.set_marks())
# obj1=Marks(-1)
# print(obj1.set_marks())
#
# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def __init__(self,age):
#         self.age = age
#     def check_aligibility(self):
#         if self.age <= 18:
#             raise InvalidAgeError
#         else:
#             return True
# c=Voter(19)
# print(c.check_aligibility())

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def withdraw(self, amount):
#         if self.balance < amount:
#             raise ValueError("Balance must be greater than or equal to zero")
#         self.balance -= amount
#         return amount
# b=BankAccount(100)
# print(b.balance)
# print(b.withdraw(100))
# print(b.balance)
# print(b.withdraw(100))

#
# class Password:
#     def validate(self, password):
#         if len(password) < 8:
#             raise TypeError("Password must be at least 8 characters")
#         return password
# o=Password()
# try:
#     print(o.validate("eee"))
# except:
#     print(o.validate("dsffrdeed"))
#
# class UserInput:
#     def get_integer(self,value):
#         try:
#             return int(value)
#         except ValueError:
#             return "value is not an integer"
#         except TypeError:
#             return "value is not a string"
# i=UserInput()
# print(i.get_integer(1))
# print(i.get_integer("adc"))
# print(i.get_integer("adc"))
# print(i.get_integer(None))


class Calculator:
    def add(self, **kwargs):
        return sum(kwargs.values())
c=Calculator()
print(c.add(a=1,b=2,c=3))
print(c.add(g=10,l=20,k=3,h=3,c=30))
