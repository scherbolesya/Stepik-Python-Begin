# Table 1
# Given a natural number n (n≤ 9). Write a program that prints a table of size n×3 consisting of a given number (numbers separated by one space).
# Note. There may be a space at the end of the line.
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3, состоящую из данного числа (числа отделены одним пробелом).
Примечание. В конце строки может быть пробел.


n = int(input())
for i in range(n):
    for i in range(3):
        print(n, end=' ')
    print()


Sample Input 1:
8
Sample Output 1:
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
Sample Input 2:
4
Sample Output 2:
4 4 4
4 4 4
4 4 4
4 4 4
Sample Input 3:
1
Sample Output 3:
1 1 1
