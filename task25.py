# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

user_input = input('Введите строку с символами (через пробел): ').split()
div = '_'
counter = 0
for letter in user_input:
    for i in range(len(user_input)):
        if letter == user_input[i]:
            if counter > 0:
                user_input[i] = letter + div + str(counter)
            counter += 1
    counter = 0
print(user_input)
