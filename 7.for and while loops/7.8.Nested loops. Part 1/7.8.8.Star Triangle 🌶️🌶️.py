# Star Triangle 🌶️🌶️
# Given an odd natural number n. Write a program that prints an isosceles star triangle with base n as shown in the example:
*
**
***
****
***
**
*
# Note. Use a nested for loop.
Звездный треугольник 🌶️🌶️
Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:

*
**
***
****
***
**
*

Примечание. Используйте вложенный цикл for.


n = int(input())
n%2!=0
for i in range(n//2):
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(n//2+1,0,-1):
    for j in range(i):
        print('*', end='')
    print()

  
Sample Input 1:
3
Sample Output 1:
*
**
*
Sample Input 2:
5
Sample Output 2:
*
**
***
**
*
