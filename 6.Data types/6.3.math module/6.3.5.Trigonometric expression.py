# Trigonometric expression
# Write a program to calculate the value of a trigonometric expression
# Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения
sinx+cosx+tan**2x
#  по заданному числу градусов x.
# by a given number of degrees x.
# Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.
# Note 2: The math module contains a built-in function radians() that converts an angle from degrees to an angle in radians.


from math import *
x = float(input())  #тригонометрическое выражение
x1 = radians(x)
cos = cos(x1)
sin = sin(x1)
tan = (tan(x1))**2
T = cos + sin + tan
print(T)


Sample Input 1:
30.0
Sample Output 1:
1.6993587371177719
Sample Input 2:
45.0
Sample Output 2:
2.414213562373095
Sample Input 3:
60.0
Sample Output 3:
4.3660254037844375
