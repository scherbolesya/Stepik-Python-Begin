# Star triangle
# Звездный треугольник
# На вход программе подается натуральное число n(n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# The input to the program is a natural number n(n≥2) – a leg of a right isosceles triangle.
# Write a program that prints a star triangle as shown in the example.


n = int(input())  
for i in range(n):
    print("*" *(n-i))


Sample Input 1:
3
Sample Output 1:
***
**
*
Sample Input 2:
11
Sample Output 2:
***********
**********
*********
********
*******
******
*****
****
***
**
*
