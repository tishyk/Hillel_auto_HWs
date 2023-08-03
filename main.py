# Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
# Імпортуйте цю функцію, і викличте в іншому файлі


def home_work_5(first, second):
    if type(first) == int and type(second) == int:
        return first * second
    elif type(first) == str and type(second) == str:
        return first + second
    else:
        return (first, second)


if __name__ == '__main__':
    b = 1
    print(b)

# # import import_exampel as ie
# from import_exampel import get_sum
#
# b = 80
# print(b)
# a = 1
# print(b + a)

# while True:
#     user_input = input('Input word:')
#     if "o" in user_input.lower():
#         break
#     else:
#         print("wrong word")

# user_input = input('Input word:')
# while "o" not in user_input and "O" not in user_input:
#     user_input = input("The:")
#
# print(f'Yas {user_input}')


# def sum(first_num, second_num, third_num = 100):
#
#     return  first_num + second_num +third_num
#
# sum_resalt = sum(1, 2)
# print(sum_resalt)

#
# def get_sum(*args):
#     return sum(args)
# def get_sum_t(num_tupel):
#     return sum(num_tupel)
#
# print(get_sum_t((1,2,3,4,6)))
#
# def get_summ_kwargs(**kwargs):
#     return sum(kwargs.values())
#
# resalt_kwargs = get_summ_kwargs(a=5, d=6)
# print(resalt_kwargs)

# print(get_sum(1, 2, 3))
