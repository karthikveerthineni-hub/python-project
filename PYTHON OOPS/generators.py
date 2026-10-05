# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1
# for num in count_up_to(5):
#     print(num)

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci()
# for _ in range(20):
#     print(next(fib))


# def numbers():
#     yield 10
#     yield 20
#     yield 30
#     yield 40

# result = numbers()

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


# def count():
#     for i in range(1, 6):
#         yield i

# for value in count():
#     print(value)


def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)