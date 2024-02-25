# Second digit
# Given a natural number n(n>9). Write a program that determines its second (from the beginning) digit.
Вторая цифра
Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.


num = int(input()) 
a = 0
b = 0
while num!=0:
    a=b
    b = num %10
    num = num//10
print(a)
  
  
Sample Input 1:
455672
Sample Output 1:
5
Sample Input 2:
59
Sample Output 2:
9
Sample Input 3:
123
Sample Output 3:
2
