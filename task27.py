# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
#
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure

uinput = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure"
print(len(set(uinput.split())))
