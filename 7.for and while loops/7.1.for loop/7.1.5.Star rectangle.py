# Star rectangle
# Звездный прямоугольник
# На вход программе подается натуральное число n.
# Напишите программу, которая печатает звездный прямоугольник размерами n×19.
# The program input is a natural number n.
# Write a program that prints a star rectangle of dimensions n×19.
# Подсказка. Для печати звездной линии используйте умножение строки на число.
# Clue. To print a star line, use multiplying the line by the number.


n = int(input())
a = "*******************"
for i in range(n):
    print(a)
  

Sample Input 1:
1
Sample Output 1:
*******************
Sample Input 2:
2
Sample Output 2:
*******************
*******************
Sample Input 3:
3
Sample Output 3:
*******************
*******************
*******************
