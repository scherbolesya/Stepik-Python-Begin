# Sum of factorials
# Given a natural number n. Write a program that prints the value of the sum 1!+2!+3!+…+n!.
# Note 1. The factorial of a natural number n is the product of all natural numbers from 1 to n, that is, n!=1⋅2⋅3⋅…⋅n
# Note 2. The problem can be solved without a nested loop. Write two versions of the program =)
Сумма факториалов
Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.
Примечание 1. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть n!=1⋅2⋅3⋅…⋅n
Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)


from math import *
n = int(input())
s=0
for i in range(1,n+1):
    s+=factorial(i)
print(s)


Sample Input 1:
3
Sample Output 1:
9
Sample Input 2:
1
Sample Output 2:
1
Sample Input 3:
2
Sample Output 3:
3
