#задание 1
#Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных будет свидетельствовать пустая строка.

my_list = []
while True:
    content = input('Введите данные: ')
    if not content:
        break
    else:
        newcontent = content + '\n'
        my_list.append(newcontent)
    with open('text.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.writelines(my_list)

with open('text.txt', 'r') as f_obj:
    text = f_obj.read()
    print(text)

#Задание 2
#Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('text_2.txt', 'r') as f_obj:
    count = 1
    for line in f_obj:
        a = len(line.split())
        print (f"Строка {count} состоит из {a} слов")
        count +=1

#Задание 3
#Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

all_salary = 0
count = 0
my_list = []
with open('text_3.txt', 'r') as f_obj:
    for line in f_obj:
        salary = line.split(':')
        if int(salary[1]) <= 20000:
            my_list.append(salary[0])
        all_salary += int(salary[1])
        count += 1
result = all_salary / count
print(f"Сотрудники с зп менее 20 тыс: {my_list}")
print(f"Средняя зп: {result}")


#задание 4
#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
my_list = []
with open('text_4.txt', 'r') as f_obj:
    for line in f_obj:
        one = line.split('-')
        word = translate.setdefault(one[0])
        my_list.append(word +' - '+ one[1])
with open('text_5.txt', 'w+') as f_obj:
    f_obj.writelines(my_list)
    f_obj.seek(0)
    text = f_obj.read()
    print(text)


#Задание 5
#Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
with open('text_6.txt', 'w+') as f_obj:
    for i in my_list:
        f_obj.write(str(i) + ' ')
    f_obj.seek(0)
    content = f_obj.read()
    n = content.split()
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    print (f'Сумма чисел в файле {summ}')


#Задание 6
#Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

title = []
number = []
my_dict = {}
with open('text_7.txt', 'r') as f_obj:
    for line in f_obj:
        name = line.split(':')
        title.append(name[0])
        #Далее код, который пробегается по каждому символу в строке и ищет цифры.
        #Если находит цифру, записывает ее в строку. Если следующий символ в строке тоже цифра,
        # то он добаляется к строке.
        l = len(line)
        integ = []
        i = 0
        while i < l:
            s = ''
            a = line[i]
            while '0' <= a <= '9':
                s += a
                i += 1
                if i < l:
                    a = line[i]
                else:
                    break
            i += 1
            if s != '':
                integ.append(int(s))
        number.append(sum(integ))
for k,v in zip(title,number):
    my_dict[k] = v
print (my_dict)


#Задание 7
#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

all_firm = []
all_profit = []
firm_losses = []
firm_profit = []
profit = []
with open('text_8.txt', 'r') as f_obj:
    for line in f_obj:
        name = line.split(' ')
        all_firm.append(name[0])
        n = int(name[2]) - int(name[3])
        if n > 0:
            firm_profit.append(name[0])
            all_profit.append(n)
            profit.append(n)
        else:
            firm_losses.append(name[0])
            all_profit.append(abs(n))
average_profit = sum(profit)/len(profit)
my_dict_1 = {}
my_dict_2 = {'average_profit': average_profit}
for k,v in zip(all_firm,all_profit):
    my_dict_1[k] = v
data = my_dict_1, my_dict_2
import json
with open('text_9.json', 'w+') as write_js:
    json.dump(data, write_js)
    json_str = json.dumps(data)
    print(json_str)



