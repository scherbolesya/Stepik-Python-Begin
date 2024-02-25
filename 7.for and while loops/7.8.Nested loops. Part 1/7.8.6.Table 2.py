# Table 2
# Given a natural number n (n≤ 9). Write a program that prints a table of size n×5, where the i-th line contains the number i (the numbers are separated by one space).
# Note. There may be a space at the end of the line.
Таблица-2
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, где в i-ой строке указано число i (числа отделены одним пробелом).
Примечание. В конце строки может быть пробел.


n = int(input()) 
for i in range(n):
    for j in range(5):
        print(i+1, end=' ')
    print()


Sample Input 1:
3
Sample Output 1:
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
Sample Input 2:
6
Sample Output 2:
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
6 6 6 6 6
Sample Input 3:
1
Sample Output 3:
1 1 1 1 1
