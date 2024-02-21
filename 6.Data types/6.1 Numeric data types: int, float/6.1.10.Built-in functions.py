Встроенные функции

Python включает много заранее определенных функций. Программист не видит их реализацию, она скрыта. Достаточно знать, как эти функции называются и что они делают.
Мы уже сталкивались с встроенными функциями:

print() — вывести на экран;
input() — считать с клавиатуры;
int() — преобразовать к целому числу;
float() — преобразовать к числу с плавающей точкой.
Рассмотрим три новые встроенные функции, которые используются достаточно часто при работе с числами.

--------------------------------------------------------------------------------------------------------
Функции min() и max()

Для определения соответственно минимального или максимального значения используются функции min() и max(). 
Аргументов у этих функций может быть любое количество, главное, чтобы они все поддерживали между собой операцию сравнения (например, float и int поддерживают сравнение, а float и str - нет).
Например, результатом выполнения следующего кода:

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)
будет:

12
-3
9.8

------------------------------------------------------------------------------------------------------
Функция abs()

Модулем (абсолютной величиной) положительного числа называется само число, модулем отрицательного числа называется противоположное ему число, 
модуль нуля – нуль. Модуль числа a обозначается ∣a∣, для него имеет место равенство:
Для нахождения модуля (абсолютной величины) числа в Python используется функция abs().
Например, результатом выполнения следующего кода:

print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))
будет:

10
7
0
17.67
Обратите внимание, все три функции max(), min(), abs() работают как с целыми числами, так и с числами с плавающей точкой.