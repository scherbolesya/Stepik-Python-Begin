# Number sequence 3 🌶️
# Последовательность чисел 3 🌶️
Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные целые числа от m до n включительно в порядке убывания.
# Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него.
# Note. Try solving the problem in two ways: using a conditional if statement and without it.

  
m = int(input())
n = int(input())
for i in range(m, n,-2):
    if i % 2 != 0:
        print(i)
    if i%2 ==0:
        print(i-1)
      
  
Sample Input 1:
77
62
Sample Output 1:
77
75
73
71
69
67
65
63
Sample Input 2:
6
-2
Sample Output 2:
5
3
1
-1
Sample Input 3:
9980
9972
Sample Output 3:
9979
9977
9975
9973
