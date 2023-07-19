
# home_work_lesson_2
new_word_1 = input("Слово :")
word_quantity = len(new_word_1)

string_word_format_1 = "Word '{word}' has {length} letters"
format_result_1 = string_word_format_1.format(word=new_word_1, length=word_quantity)

print(format_result_1)
