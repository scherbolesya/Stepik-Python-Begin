# Fibonacci Sequence 🌶️
Последовательность Фибоначчи 🌶️
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
Примечание. Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих:
1, 1, 2, 3, 5, 8, 13,  21, 34, 55, 89,…
# Write a program that reads a natural number n and prints the first n numbers of the Fibonacci sequence.
# Note. The Fibonacci sequence is a sequence of natural numbers, where each subsequent number is the sum of the previous two:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,…


x = 1 
a = 1
b = 1
for i in range(1,int(input())+1):
    if i<=2: x=1; a=1; b=1;
    if i>2: x=a+b; a=b; b=x;
    print(x, end=' ')
  

Sample Input 1:
1
Sample Output 1:
1
Sample Input 2:
5
Sample Output 2:
1 1 2 3 5
Sample Input 3:
22
Sample Output 3:
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711
