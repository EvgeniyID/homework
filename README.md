#Задание 1
#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
#Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
#Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

file_name, worked_hour, rate, benefit = argv

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Ваша суммарная зарплата: {calculation}")

#Задание 2
#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].

my_list = [4, 223, 5, 54, 1, 1, 3, 457, 7, 89, 55, 312, 23, 232, 33]
new_list = [i for i in my_list if i > my_list[my_list.index(i)-1]]
print(new_list)

#или

my_list = [1, 1, 2, 2, 2, 3, 3, 3, 44, 54, 22, 43, 5745, 2, 1, 0, 434, 5, 54, 44]
a = 0
new_list= []
for i in my_list:
    if i > my_list[a-1]:
        new_list.append(i)
    a+=1
print(new_list)

#Задание 3
#Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

print (f'Числа от 20 до 240 кратные 20 или 21 - {[i for i in range(20, 240) if i%20==0 or i%21==0]}')

#Задание 4
#Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
#Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [i for i in my_list if my_list.count(i) == 1]
print(new)

#Задание 5
#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce
new = [i for i in range(100, 1001) if i % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el
print (reduce(my_func, new))

#Задание 6
#Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. ####
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from itertools import count

def count_func(start_number, stop_number):
    for i in count(start_number):
        if i > stop_number:
            break
        else:
            print(i)

from itertools import cycle

def cycle_func(my_list, stop):
    count = 0
    iter = cycle(my_list)
    while count < stop:
        print(next(iter))
        count += 1
count_func(start_number = int(input('Введите начальное число: ')), stop_number = int(input('Введите конечное число: ')))
cycle_func(my_list = [1, 2, 'foo', True, 3], stop = int(input("Введите количество повторений: ")))

#Задание 7
#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

n = int(input('Введите n: '))
from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

mygenerator = fact()
a = 0
for i in mygenerator:
    if a < n:
        print(i)
        a += 1
    else:
        break
