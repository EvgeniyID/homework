#Задание 1
#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


spisok = [1, 2.5, 3, 'цифра', True, None]
for i in range(len(spisok)):
    print (type(spisok[i]))

#Задание 2
#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().

a = int(input('Введите количество элементов в всписке: '))
spisok = []
for i in range(a):
    spisok.append(input('Введите данные: '))
    i += 1
el = 0
for i in range(a//2):
    spisok[el], spisok[el + 1] = spisok[el + 1], spisok[el]
    el +=2
print (spisok)

#или

a = input('Введите данные через пробел: ')
spisok = a.split()
for i in range(0, len(spisok)//2, 2):
    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
print (spisok)

#Задание 3
#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

a = int(input('Введите номер месяца: '))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
if a == 1 or a == 2 or a == 12:
    print (seasons_list[0])
elif a == 3 or a ==4 or a ==5:
    print (seasons_list[1])
elif a == 6 or a ==7 or a ==8:
    print (seasons_list[2])
elif a == 9 or a ==10 or a ==11:
    print (seasons_list[3])
else:
    print ('Такого месяца не существует!')

a = int(input('Введите номер месяца: '))
seasons_dict = {1: 'Зима', 2: 'Весна', 3 : 'Лето', 4 : 'Осень'}
if a == 1 or a == 2 or a == 12:
    print(seasons_dict.get(1))
elif a == 3 or a ==4 or a ==5:
    print(seasons_dict.get(2))
elif a == 6 or a ==7 or a ==8:
    print(seasons_dict.get(3))
elif a == 9 or a ==10 or a ==11:
    print(seasons_dict.get(4))
else:
    print ('Такого месяца не существует!')

#Задание 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

stroka = input('Введите несколько слов через пробел: ')
my_list = stroka.split()
num = 1
for i in range(len(my_list)):
    if len(str(stroka)) <= 10:
        print(f" {num} {my_list [i]}")
        num += 1
    else:
        print(f" {num} {my_list [i] [0:10]}")
        num += 1

#Задание 5
#Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
a = int(input('Введите число (0 - выход): '))
while a != 0:
    for i in range (len(my_list)):
        if a >= my_list[0]:
            my_list.insert(0, a)
            break
        elif a <= my_list[-1]:
            my_list.append(a)
            break
        elif a <= my_list[i] and a >= my_list [i+1]:
            my_list.insert(i+1, a)
    print (my_list)
    a = int(input('Введите число: '))

#Задание 6
#Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
#Структуру нужно сформировать программно, запросив все данные у пользователя.

my_list =[]
while input("Желаете добавить товар? press y/n: ") == 'y':
    number = int(input("Введите номер товара: "))
    my_dict = {}
    list_1 = []
    list_2 = []
    while input("Желаете добавить параметры товара? press y/n: ") == 'y':
        list_1.append(input('Введите параметр товара: '))
        list_2.append(input('Введите значение параметра: '))
    for i in range(len(list_1)):
        my_dict[list_1[i]] = list_2[i]
    my_list.append((number, my_dict))
print (my_list)
analitic = {}
for el in my_list:
    for list_1, list_2 in el[1].items():
        if list_1 in analitic:
            analitic[list_1].append(list_2)
        else:
         analitic[list_1] = [list_2]
print(analitic)
