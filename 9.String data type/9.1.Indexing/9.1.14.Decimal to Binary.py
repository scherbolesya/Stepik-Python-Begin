Decimal to Binary
На вход программе подается натуральное число, записанное в десятичной системе счисления. 
Напишите программу, которая переводит данное число в двоичную систему счисления.
# The input to the program is a natural number written in the decimal number system. Write a program that converts a given number to the binary number system.

n = int(input()) 
b = ''
while n > 0:
    b=str(n%2)+b
    n=n//2
print(b)


Sample Input 1:
5
Sample Output 1:
101
Sample Input 2:
128
Sample Output 2:
10000000
