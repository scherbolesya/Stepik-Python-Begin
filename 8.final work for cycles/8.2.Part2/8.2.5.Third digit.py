# Third digit
# Given a natural number n(n>99). Write a program that determines its third (from the beginning) digit.
Третья цифра
Дано натуральное число n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.


n = int(input())
n>99
a=n
while a > 999:
        a= a //10
print(a%10)
  
  
Sample Input 1:
100000000
Sample Output 1:
0
Sample Input 2:
3459087654
Sample Output 2:
5
Sample Input 3:
134
Sample Output 3:
4
