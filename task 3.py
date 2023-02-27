def city():
    x = ["Astana", "Moskwa", "Kiev", "Minsk", "Tashkent", "Bishkek", "Pekin", "Ankara", "Tegeran", "Baku"]
    for i in range(len(x)):
        print(x[i])
city()

#2
class Student:
    def __init__(self):
        self.fio = ""
        self.cls = ""
    def __init__(self, fio):
        self.fio = fio
        self.cls = ""
    def __init__(self, fio, cls):
        self.fio = fio
        self.cls = cls
    def __str__(self):
        return "ФИО: "+ self.fio +" Класс: "+ self.cls

studentList = []
#Инструкция запросов
while True:
    print("+ - Добавить учащегося\nl - Вывести список учащихся\ns - Вывести отсортированный список учащихся\nq -Выход")
    cmd = input()
#Обработка команд
    if cmd == "+":
        print("ФИО:")
        fio = input()
        print("Класс")
        cls = input()
        st = Student(fio, cls)
        studentList.append(st)
#Вывод списка без сортировки
    elif cmd == "l":
        print("------Список учащихся------")
        for student in studentList:
            print(student)
        print("------")
#Вывод сортированного списка
    elif cmd == "s":
        sortedList = studentList
        sortedList.sort(key = lambda x: x.cls)
        print("------Список учащихся------")
        for student in sortedList:
            print(student)
        print("------")
    elif cmd == "q":
        break
#3
str = str(input())
upper = 0
lower = 0
for i in str:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(str.upper())
else:
    print(str.lower())

#
a, b = input(), input()
while not(a.isdigit() and b.isdigit()):
    a, b = input(), input()
print(int(a) + int(b))
