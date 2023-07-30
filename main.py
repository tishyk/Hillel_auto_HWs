#lesson_4_homework
# 1. Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".


# task_1_v1
task1_str = input("Enter the word with letter 'o' in English or Resend languish:")
counter = 0
for element_task1 in task1_str:
    if element_task1 == "o" or element_task1 == "O" or element_task1 == "о" or element_task1 == "О":
        counter += 1


print(f"Word '{task1_str}' contains {counter} letters 'o'")


# task_1_v2
while True:
    task1_str = input("To stop enter a word with the letter 'o' English or Resend languish:")
    if 'o' or 'о' in task1_str.lower():
        break

counter_en = task1_str.lower().count('o')
counter_ru = task1_str.lower().count('о')
total_counter = counter_ru + counter_en
print(f"Word '{task1_str}' contains {total_counter} letters 'o'")


# 2.Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

# task_2 v1
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for item in lst1:
    if type(item) != str:
        continue
    else:
        lst2.append(item)
print(lst2)





# 3. Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
list_num = [1, 11, 21, 31, 100]
sum_list = 0
for num in list_num:
    if (num % 2) == 0:
        sum_list += num
    else:
        continue
print(sum_list)



# test_string = "asd"
# test_list = ["asd", "my name is Dima", "Python is good"]

# for char in test_string:
#     if char == "a":
#         continue
#     print(char)

# for test_in_list in test_list:
#     for letter in test_in_list:
#         print(letter)

#
# test_dict = {1: "name", 2: "name2"}
# for dict_element in test_dict.items():
#     print(dict_element)



# counter = 1

# while counter <= 10:
#     print(counter)
#     counter += 1




# while True:
#     print(counter)
#     if counter >= 10:
#         break
#     counter += 1
#
# test_string = "asd vcx"
# result_str = ""
# counter = 0
# while counter <= len(test_string)-1:
#     if test_string[counter] == " ":
#         counter += 1
#         continue
#     else:
#         result_str += test_string[counter]
#         counter += 1
# print(result_str)





# text = input("Enter text:")
# uniq_symbols = set(text)
#
# if len(uniq_symbols) > 10:
#     print(True)
# else:
#     print(False)
#
# print(len(set(input("Enter text"))) > 10)