# numbers = [1, 2, 3, 4]
# result = map(lambda x: x * 2, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5]
# result = map(lambda x: x**2, numbers)
# print(list(result))

# numbers = [10, 20, 30]
# result = map(str, numbers)
# print(list(result))

# names = ["Ram", "Krishna", "Arjun"]
# result = map(len, names)
# print(list(result))

# names = ["python", "java", "c"]
# result = map(str.upper, names)
# print(list(result))

# numbers = [5, 10, 15]
# result = map(lambda x: x + 10, numbers)
# print(list(result))

# a = [1, 2, 3]
# b = [4, 5, 6]
# result = map(lambda x, y: x + y, a, b)
# print(list(result))

# numbers = [10, 15, 20, 25]
# result = map(lambda x: x % 2 == 0, numbers)
# print(list(result))

# celsius = [0, 20, 30, 40]
# result = map(lambda c: int(c * 9/5) + 32, celsius)
# print(list(result))

# numbers = [10, 20, 30]
# result = map(id, numbers)
# print(list(result))

# def cube(n):
#     return n ** 3
# numbers = [1, 2, 3, 4]
# result = map(cube, numbers)
# print(list(result))

# def square(n):
#     return n ** 2
# result = map(square, numbers)
# print(list(result))

# def multiply(n):
#     return n ** 2
# result = list(map(multiply, numbers))
# print(result)

# def divide(n):
#     return n // 2
# result =list( map(divide, numbers))
# print(result)

# students = [
#     ("Ram", 90),
#     ("Sita", 85),
#     ("Arjun", 95)
# ]
# result = map(lambda x: x[1], students)
# print(list(result))

# students = [
#     ("Ram", 90),
#     ("Sita", 85),
#     ("Arjun", 95)
# ]
# result = map(lambda x: x[0], students)
# print(list(result))
git
# nested_list = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda sublist: list(map(lambda x: x + 5, sublist)), nested_list))
# print(result)

# nested_list = [[1, 2], [3, 4], [5, 6]]
# result = [list(map(lambda x: x + 5, sublist)) for sublist in nested_list]
# print(result)

text = "Python"
result = list(map(ord, text))
print(result)