# Together
# A natural number is given. Write a program that calculates:
# - the sum of its digits;
# - the number of digits in it;
# - the product of its digits;
# - arithmetic mean of its digits;
# - its first digit;
# - the sum of its first and last digits.
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:
- сумму его цифр;
- количество цифр в нем;
- произведение его цифр;
- среднее арифметическое его цифр;
- его первую цифру;
- сумму его первой и последней цифры.


num = int(input())
a1 = num 
a = 0 #сумму его цифр;
b = 0 #количество цифр в нем;
c = 1 #произведение его цифр;
d = 0 #среднее арифметическое его цифр;
e = a1%10 #последняя цифра
s = 0 #его первую цифру;
while num != 0:
    s = num % 10
    a +=s
    b += 1
    c *=s
    num = num //10
print(a)
print(b)
print(c)
print(a/b) #среднее арифметическое его цифр;
print(s)
print (e+s)


Sample Input 1:
5678
Sample Output 1:
26
4
1680
6.5
5
13
Sample Input 2:
132
Sample Output 2:
6
3
6
2.0
1
3
Sample Input 3:
75
Sample Output 3:
12
2
35
6.0
7
12
