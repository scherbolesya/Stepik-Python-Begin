Цифра 1
# Digit 1
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
# The input to the program is one line consisting of numbers. Write a program that calculates the sum of the digits of a given string.

n = input()
a =int(n)
s = 0
while a>0:
    s = a%10+s
    a = a//10
print(s)


Sample Input:
2514
Sample Output:
12
