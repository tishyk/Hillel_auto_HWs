# Write generator, which generates numbers in a given range (from a certain number to a certain number)


def new_generator_homework8(num1, num2):
    while True:
        if num1 > num2:
            break
        else:
            yield num1
            num1 += 1


for el in new_generator_homework8(5, 10):
    print(el)

# def get_test_mail(count):
#     num = 0
#     while num <= count:
#         yield num
#         num += 1
# for el in get_test_mail(5):
#     print(el)

# def get_suquare(limit):
#     num = 1
#     while num <= limit:
#         yield num ** 2
#         num += 1
#
# for el in get_suquare(5):
#     print(el)

# import datetime
# import time
# def get_test_mail(count):
#
#     num = 1
#     while num <= count:
#         time.sleep(0.1)
#         yield f"testmail{datetime.datetime.now()}@gmail.com"
#         num += 1
#
# for el in get_test_mail(5):
#     print(el)


# def parametr_decorator(n):
#     def new_decrator(func1):
#         def decorator_wrapper(*args, **kwargs):
#             print(f"before {n}")
#             func1(*args, **kwargs)
#             print(f"after {n}")
#         return decorator_wrapper
#     return new_decrator
#
# @parametr_decorator(5)
# def print_hello(word_to_print):
#     print(word_to_print)
#
# print_hello("Hello")
