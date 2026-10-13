'''• Write a Python program using a context manager (with)
 to open a text file in read mode,
 read the entire content using read(),
 and print the number of characters in the file.'''

with open("test.txt","r") as f:
    print(f.read())
    f.seek(0)
    d=f.read()
    print("no of characters:",len(d))

''' Write a program that opens a file using 
a context manager, reads all lines using readlines(), 
and prints only the 
lines that contain more than 10 characters.'''
#
# with open("test.txt","r") as f:
#     r=f.readlines()
# for line in r:
#     if len(line)>10:
#         print(line)

'''• Write a program that creates a file and writes 3
 lines using write(), reopens the same file in append mode,
  appends 2 more lines, and 
finally reads and prints the complete file content.'''
#
# with open("test.txt","w") as f:
#     f.write("hello bro\n")
#     f.write("Nice\n")
#     f.write("python\n")
# with open("test.txt","a") as f:
#     f.write("hello bro\n")
#     f.write("Nice\n")
# with open("test.txt","r") as f:
#     print(f.read())

'''• Create a custom context manager using a class
 that opens a file in write mode in the __enter__ method, 
 writes a line to the file, closes the file in the __exit__ method,
  and properly prints or logs 
any exception information received in __exit__.'''
#
# class MyClass:
#     def __init__(self,fn):
#         self.fn= fn
#     def __enter__(self):
#         print("Opening file...")
#         self.f=open(self.fn, 'w')
#         self.f.write("Hello World")
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Closing file...")
#         self.f.close()
# my_obj = MyClass("test.txt")
# with my_obj as f:
#     print("Hello World")

''' Create a custom context manager using @contextmanager
 from the contextlib module that opens a file,
  yields the file object, and ensures 
the file is closed even if an exception occurs.'''

# from contextlib import contextmanager
# @contextmanager
# def open_file(fn):
#     f=open(fn,'r')
#     try:
#         yield f
#     finally:
#         print('goodbye')
#         f.close()
# with open_file('test.txt') as f:
#     print(f.read())

'''Write a program using a context manager
 that opens a file in read mode, uses a loop
  to read the file in small chunks 
  (for example, 5 characters at a time),
   prints the cursor position after each read using
    tell(), uses seek() to move to a specific position, 
and continues reading from there.'''
with open('test.txt', 'r') as f:
    while True:
        data = f.read(5)
        if not data:
            break
        print("Data:", data)
        print("Position:", f.tell())
    f.seek(3)
    print("After seek:", f.tell())
    data = f.read(5)
    print("Data after seek:", data)
    print("Position:", f.tell())








