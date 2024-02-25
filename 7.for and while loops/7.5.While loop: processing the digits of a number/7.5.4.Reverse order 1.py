# Reverse order 1
# A natural number is given. Write a program that displays its numbers in a column in reverse order.
Обратный порядок 1
Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.


num = int(input())
while num != 0:
    a = num % 10
    print(a)
    num= num //10


Sample Input 1:
12345
Sample Output 1:
5
4
3
2
1
Sample Input 2:
55690454
Sample Output 2:
4
5
4
0
9
6
5
5
Sample Input 3:
9673210458
Sample Output 3:
8
5
4
0
1
2
3
7
6
9
