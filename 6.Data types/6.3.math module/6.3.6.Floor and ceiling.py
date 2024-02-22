# Floor and ceiling
# # Write a program that calculates the value of ⌈x⌉ +⌊x⌋ given a real number x.

# Пол и потолок
# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.


from math import * # пол т потолок
x = float(input())
a = floor(x)
b = ceil(x)
c = a+b
print(c)


Sample Input 1:
5.5
Sample Output 1:
11
Sample Input 2:
5.4
Sample Output 2:
11
Sample Input 3:
-12.2
Sample Output 3:
-25
