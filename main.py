# Написати функцыю, яка буде рекурсивно вираховувати число фібоначчі.
#
# Число фібоначчі - це число, яке дорівнює суммі двох попередніх в послідовності (це і повинно бути в рекурсії). Закінчується на двох одиницях


def new_fibanacci_fan(num:int):
    if num == 1 or num == 2:
        return 1
    elif num == 0:
        return 0
    else:
        return new_fibanacci_fan(num-1) + new_fibanacci_fan(num-2)

resalt = new_fibanacci_fan(9)
print(resalt)



# def fibonacci_num(numer_fib):
#     if numer_fib == 1 or numer_fib == 2:
#         return 1
#     else:
#         return fibonacci_num(numer_fib-1) + fibonacci_num(numer_fib-2)
#
# result = fibonacci_num(9)
# print(result)
#
#
# def fibonacci_even(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci_even(n - 1) + fibonacci_even(n - 2)
#
# print(fibonacci_even(7))

# def  weit_for():
#     text = input("Enter qwe:")
#     if text == "qwe":
#         return text
#     else:
#         return weit_for()
#



#
# def  weit_for_1():
#     while True:
#      text = input("Enter qwe: ")
#      if text == "qwe":
#         return text
#
# weit_for_1()

# def add_to_num(namder: int):
#     print(namder)
#     if (namder == 500):
#         return namder
#     else:
#         namder += 2
#         add_to_num(namder)
# # sys.setrecursionlimit(10500)
#
# add_to_num(499)


# def sum_to_num(number):
#     return number + 10
#
# updated_nam = lambda number: number + 10
#
# print(sum_to_num(0))
# print(updated_nam(0))