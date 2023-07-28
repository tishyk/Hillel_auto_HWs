# lesson_3_homework
#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

homework_3 = set(input("Введите значения:"))
if int(len(homework_3)) > 10:
    print(True)
elif int(len(homework_3)) <= 10:
    print(False)
else:
    print("Введено неверное значение")


# #Set_unordered
# sel_example = {'test', 1, 2, True, True}
# print(sel_example)
#
#
# list_example = ["test@gmail.com", "test@gmail1.com", "test@gmail.com"]
# set_from_list = list(set(list_example))
# print(list_example)
# print(set_from_list)
# tuple_from_list = tuple(list_example)
# print(tuple_from_list)
# print(list('asd'))


# #tuple_ordered_unchangeable
# tuple_example = (123, 'apple', True, 123)
# print(tuple_example)
# print(tuple_example[0])



# dict_lesson_3_unordered_changeable
# employers_dict = {"test@gmail.com": "Test 1",
#                   "test1@gmail.com": "Test 2",
#                   "test2@gmail.com": "Test3",
#                   1: "Test4",
#                   2: 76}
#
# print(employers_dict)
# print(employers_dict["test@gmail.com"])
# print(employers_dict[1])
# employers_dict[2] = 5
# employers_dict[1] = "New value"
# print(employers_dict[2])
# print(employers_dict[1])
# print(len(employers_dict)) # Чего длинна







# #List_lesson_3_ordered_changeable
# list_example_int = [1, 2, 5, 8]
# list_example_str = ['apple', 'banana']
# list_example_mix = [1, 'apple']
# # print(list_example_int)
# # print(list_example_str)
# # print(list_example_mix)
# print(list_example_mix[1])
# list_example_mix[1] = 'strawberry'
# print(list_example_mix[1])



# #lesson_3_if_else
# first_num = int(input('Enter first num:'))
# second_num = int(input('Enter second num:'))
#
# if first_num > second_num:
#     print(True)
#     print("first number more than second number")
# elif first_num < second_num:
#     print("second number more than first number")
#     print(False)
# else:
#     print("Equal")




# input_example = input("Enter name:")
# # example_string = 'Dima' # Зачем это?
# result = f'Word {input_example} has {len(input_example)} letters'
# result_format = 'Word {word} has {len_word} letters'.format(word=input_example, len_word=len(input_example))
# print(result_format)

# print(f'Word {(input_word := input("Enter word:"))}  has {len(input_word)} letters')