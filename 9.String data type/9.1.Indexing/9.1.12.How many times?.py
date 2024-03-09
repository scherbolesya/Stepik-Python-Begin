Сколько раз?
# How many times?
На вход программе подается одна строка. Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *.
# One line is given as input to the program. Write a program that determines how many times + and * appear in a string.

n = input()
a = 0
b = 0
for s in n:
    if s == '*':
        a+=1
    elif s == '+':
        b+=1
print('Символ + встречается', b, 'раз')
print('Символ * встречается', a, 'раз')


Sample Input:
bcd+a++++**31415
Sample Output:
Символ + встречается 5 раз
Символ * встречается 2 раз
