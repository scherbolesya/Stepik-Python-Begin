# Ordered numbers 🌶️
# A natural number is given. Write a program that determines whether the sequence of its digits, 
# when viewed from right to left, is ordered in non-decreasing order.
Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр 
при просмотре справа налево упорядоченной по неубыванию.


n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n <= 9 else 'NO')


Sample Input 1:
5321
Sample Output 1:
YES
Sample Input 2:
7820
Sample Output 2:
NO
