# Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое из них четным или нет.
# Write a program that reads a sequence of 10 integers and determines whether each one is even or not.

  
counter = 0
for i in range(1,11):
    n = int(input())
    if n%2 == 0:
        counter = counter + 1
if counter == 10:
    print("YES")
else:
    print('NO')
  
  
Sample Input 1:
2
4
6
8
10
12
14
16
18
20
Sample Output 1:
YES
Sample Input 2:
1
2
3
4
5
6
7
8
9
10
Sample Output 2:
NO
