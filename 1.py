# -*- coding: utf-8 -*-
"""Копия блокнота ""Практика 0.2.0 .ipynb""

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WmTVI3bxv7LuS1Uf9R5O8_chIFt_lMKn

Напишите свое ФИО:

Кучерявин Кирилл Владимирович
"""

print('Кучерявин Кирилл Владимирович.ПИИ')

"""# Основы

Задание 1: Напиши программу, выводящую на экран сообщение "Привет, мир!"
"""

print('Привет,мир!')

"""Задание 2: Напиши программу которая запрашивает имя пользователя и выводит сообщение:

`Привет, <Имя пользователя>`
"""

a = str(input('напишите свое имя: '))
print('Привет, ', a)

"""Задание 3: Напиши программу определяющую является ли число четным или нечетным:

Пример:

`Введите число:` 2

`Ваше число четное!`
"""

a = int(input('Введите целое число: '))
if a % 2 == 0:
  print('Ваше число четное!')
else:
  print('Ваше число не четное!')

"""Задание 4: Напишите программу которая запрашивает длинну и ширину прямоугольника и выводит его площадь:



`Введите длинну прямоугольника:`

`Введите ширину прямоугольника:`

`Площадь прямоугольника: `


"""

a = float(input('Введите длинну прямоугольника(если число дробное писать через точку): '))
b = float(input('Введите ширину прямоугольника(если число дробное писать через точку): '))
print("площадь прямоугольника: ", a*b)

"""Задание 5: Напишите программу, которая будет вычислять среднее арифметическое введенных чисел"""

a = 1
d = 0
c = 0
while a == 1:
  print('вводите числа по одному, после каждого нажимайте ентер, когда напишите все числа нажмите ентер еще раз')
  b = str(input(':'))
  if b != '':
    d += float(b)
    c += 1
  if b == '':
    break


print(d/c)

"""Задание 6: Напиши программу, которая бы определяла является ли год високосным"""

a = int(input('Введите год только цифрами!!: '))
if a % 100 == 0:
  if a % 400 == 0:
    print('yes')
  else:
    print('no')
else:
  if a % 4 == 0:
    print('yes')
  else:
    print('no')

"""Задание 7: Необходимо создать простой калькулятор, который позволяет пользователю выбрать одну из четырёх операций (+, -, *, /), ввести два числа и получить результат выполнения операции."""

operachion = input('Введите только одну из предложенных операций!!! - (+, -, *, /): ')
first_num = float(input('Введите первое число(можно использовать только цифры, дробные через точку!!: )'))
second_num = float(input('Введите второе число(можно использовать только цифры, дробные через точку!!: )'))
if operachion == '+':
  print(first_num + second_num)
if operachion == '-':
  print(first_num - second_num)
if operachion == '*':
  print(first_num * second_num)
if operachion == '/':
  print(first_num / second_num)

"""# Практика 0.2.1

**Шахматы**

Даны стартовые и конечные координаты, а также фигура

Необходимо определить, может ли заданная фигура так ходить?
"""



"""# Практика 0.2.2

**Цифра на определенном месте:**

Последовательно записан натуральный ряд чисел.

Какая цифра стоит в N позиции
"""

a = input("Введите числа через пробел!!!(можно использовать только цифры и прбел): ")
b = a.split()
s = ''
for i in b:
  s = s + i
c = int(input('Введите позицию которую хотите увидеть(можно использовать при вводе только цифры!!): '))
if len(s) < c:
  print("Такой позиции нет!!")
else:
  print('Ваша цифра: ', s[c - 1])

"""# Практика 0.2.3


Возьмите код из задания 7 и улучшите ваш калькулятор следующим образом:

Пользователь вводит строку вида:

(5+5)*5 - данная строка содержит в себе математическое выражение, а также скобки

Ваша программа должная понять что за математическое выражение записано, проверить верно ли оно записано (пример неверного заполнения: (5(+)5)*5, а также расчитать его в соотвествии с правилами математики
"""


