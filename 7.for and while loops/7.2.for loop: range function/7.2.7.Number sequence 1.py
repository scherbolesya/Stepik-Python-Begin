# Number sequence 1
# Последовательность чисел 1
Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно.

  
n = int(input())
m = int(input())
for i in range(n, m+1):
    print(i)
  
  
Sample Input:
1
9
Sample Output:
1
2
3
4
5
6
7
8
9
