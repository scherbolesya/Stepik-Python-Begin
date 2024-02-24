# Largest numbers 🌶️🌶️
Наибольшие числа 🌶️🌶️
На вход программе подается натуральное число n, а затем n различных натуральных чисел последовательности, каждое на отдельной строке. 
Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
# The input to the program is a natural number n, and then n different natural numbers of the sequence, each on a separate line.
# Write a program that prints the largest and second largest numbers in a sequence.


largest = 0 
smallest = 0
n = int(input())
for i in range(1,n+1):
    n = int(input())
    if largest < n:
        smallest = largest
        largest = n 
    elif smallest < n:
        smallest = n
print(largest)
print(smallest)


Sample Input 1:
5
1
2
3
4
5
Sample Output 1:
5
4
Sample Input 2:
8
9
7
5
4
3
2
78
1
Sample Output 2:
78
9
Sample Input 3:
13
1
2
3
5
8
233
13
21
34
377
55
89
144
Sample Output 3:
377
233
