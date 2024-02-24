#  Factorial
Факториал
На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
# The program input is a natural number n. Write a program that calculates n!.
Примечание. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть n!=1⋅2⋅3⋅…⋅n
# Note. The factorial of a natural number n is the product of all natural numbers from 1 to n, that is, n!=1⋅2⋅3⋅…⋅n


total =1
for i in range(1,int(input())+1):
    total *=i
print(total)


Sample Input 1:
3
Sample Output 1:
6
Sample Input 2:
1
Sample Output 2:
1
Sample Input 3:
2
Sample Output 3:
2
