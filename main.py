# Create a file with numbers (in a few rows)
#
# Read this file, and print the sum of all numbers (create a new function for it)
#
# Use try\except block to avoid other symbols except numbers in the file


with open("num.txt", "w") as file_num:
    file_num.write('6\n')
    file_num.write('7\n')
    file_num.write('8\n')


def home_work_7():
    try:
        with open("num.txt", "r") as file_num:
            result = file_num.readlines()
            result_array = []
            total = 0
        for element in result:
            result_array.append(element.replace("\n", ""))
        for element_new in result_array:
            total += int(element_new)
        return total
    except FileNotFoundError:
        print("The file 'num.txt' does not exist.")
    except:
        print("The user added a str to the file")


new_hom = home_work_7()
print(new_hom)

# try:
#     file = open("new_text.txt")
#     print(file.readlines())
# except UnicodeDecodeError:
#     pass
# finally:
#     file.close()
#
# with open("new_text.txt", "w") as file:
#     file.write("asd\n")
#     file.write("My name Dima\n")
# with open("new_text.txt", "a") as file:
#     file.write("asd")
#     file.write("new data\n")
# with open("new_text.txt", "r") as file:
#     result =file.readlines()
#
# result_array = []
# for r in result:
#     result_array.append(r.replace("\n", ""))
#
# print(result_array)

# try:
#     print(int(input("First"))/int(input("Second")))
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Not int")
# except:
#     pass
# finally:
#     print("Finally")
#
# print("asd")

# while True:
#     try:
#         resalt = input("Enter a number: ")
#         inr_resalt = int(resalt)
#         print(inr_resalt)
#         break
#     except:
#         continue
