#Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep
class TrafficLight:
    _color = None
    _colors = ['Красный', 'Желтый', 'Зеленый']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        a=0
        while a<3:
            for i in TrafficLight._colors:
                if a % 2 == 0:
                    sleep(2)
                    print(i)
                elif a % 3 == 0:
                    sleep(5)
                    print(i)
                else:
                    sleep(7)
                    print(i)
                a +=1

traffic = TrafficLight()
traffic.running()
'''

#Задание 2
#Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
#проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т
'''
class Road:
    def __init__(self,lenght, width):
        self._lenght = lenght
        self._width = width
    def volume(self):
        self.thinkness = 0.005
        self.massa = 25
        x = self._lenght * self._width * self.massa * self.thinkness / 1000
        print (f'Для строительства дороги необходимо {x} тонн асфальта')
a_1 = Road(20,5000)
a_2 = Road(100000,5)
a_1.volume()
a_2.volume()
'''

 #Задание 3
 #Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и
# ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return 'Полное имя: ' + self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
a = Position('Петр', 'Козлов', 'Разнорабочий', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
'''

#Задание 4
