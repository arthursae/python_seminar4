# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

uinput = list(map(int, input('Введите кол-во элементов для каждого множества (через пробел): ').split()))
list_of_lists = []
temp_list = []
i = 0
for length in uinput:
    for j in range(length):
        temp_list.append(int(input('Введите число ' +
                                   str(j + 1) + ' из ' +
                                   str(length) + ' для ' +
                                   str(i + 1) + '-го множества: ')))
    list_of_lists.append(temp_list.copy())
    temp_list.clear()
    i += 1
result = []
for unordered_list in list_of_lists:
    for number in unordered_list:
        if number not in result:
            result.append(number)
result.sort()
print(result)
