# Number sequence 2 🌶️
# Последовательность чисел 2 🌶️
Даны два целых числа m и n. Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае.

  
m = int(input()) #Даны два целых числа mm и nn. Напишите программу, которая выводит все числа от mm до nn включительно в порядке возрастания, если m < nm<n, или в порядке убывания в противном случае.
n = int(input())  #Последовательность чисел 2 🌶️
if m<n:
    for i in range (m, n+1):
        print(i)
elif n<m:
    for i in range (m,n-1,-1):
        print(i)
elif n==m:
    print(m)
  
  
Sample Input 1:
1
5
Sample Output 1:
1
2
3
4
5
Sample Input 2:
7
1
Sample Output 2:
7
6
5
4
3
2
1
Sample Input 3:
100
100
Sample Output 3:
100
