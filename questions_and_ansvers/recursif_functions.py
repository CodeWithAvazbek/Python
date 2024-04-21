# result = True
# while result:
#     def fact(n):
#         if n < 0:
#             return -1
#         elif n < 2:
#             return 1
#         else:
#             return n * fact(n-1)
#
#     numbers = int(input("Enter a number: "))
#     print(fact(numbers))


def EvenNums(num):
    if num <= 0:
        return 0
    elif num % 2 == 0:
        return num + EvenNums(num - 2)
    else:
        return EvenNums(num - 1)


a = 16
print(EvenNums(a))
