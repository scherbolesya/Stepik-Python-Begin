# Reverse order 2
# A natural number is given. Write a program that reverses the order of the digits of a number.
Обратный порядок 2
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.


num = int(input())
a = 0
b = ''
while num != 0:
    a = num % 10
    b = b + str(a)
    num = num // 10
print(b)
  
  
Sample Input 1:
5086334
Sample Output 1:
4336805
Sample Input 2:
450098
Sample Output 2:
890054
Sample Input 3:
5088531157
Sample Output 3:
7511358805
