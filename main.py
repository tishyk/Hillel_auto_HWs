# # lesson 2
# # print("dima" in "my name is Dima")
#
# # test_string_procent = "my name is Dima, my age is %s, %s I'm lived in Odessa"
#
#
# #
# # print(test_string.upper())
# # print(test_string.lower())
# # print(test_string.startswith("name", 3))
# # print(test_string.endswith('Dima'))
#
# # print(test_string_procent + '27')
# # print(test_string_procent + str(27))
# #
# # procent_result = test_string_procent % (27 , 30)
# # print(procent_result)
# # print(test_string_procent.capitalize())
#
#
# # test_string_format = "my name is Dima, my age is {}, I'm lived in {}"
# # test_string_format_2 = "my name is Dima, my age is {age}, I'm lived in {city}"
# #
# # format_result = test_string_format.format(27, 'Odessa')
# # format_result = test_string_format_2.format(age=27, city='Odessa').capitalize()
# # print(format_result)
#
# my_age = 33
# test_string_fstring = f"my name is Dima, my age is {my_age}, {'something'}, {True}"
# # print(test_string_fstring)
# #
#
# print(test_string_fstring.capitalize())
# print(test_string_fstring.title())
# print(test_string_fstring.count('my'))
# string_length_exampel = len(test_string_fstring)
# print(f'symbols count: {string_length_exampel}')
#
# print(test_string_fstring.find("name"))
# int_str = "123"
# str_str = "asd"
# alnum_str = "asd"
# print(int_str.isnumeric())
# print(str_str.isalpha())
# print(alnum_str.isalnum())


test_str = "abc123456789"
# print(test_str[0])
# print(test_str[5])
# print(test_str[1:10])
# print(test_str[2:7:2])
print(test_str[-1])
print(test_str[-8:-1:2])
