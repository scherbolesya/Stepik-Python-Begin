# List of numbers
# The input to the program is one number n. Write a program that prints the list [1, 2, 3, ..., n].
Список чисел
На вход программе подается одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].

n = int(input())
a = list(range(1,n+1))
print(a)


Sample Input 1:
1
Sample Output 1:
[1]
Sample Input 2:
5
Sample Output 2:
[1, 2, 3, 4, 5]
Sample Input 3:
10
Sample Output 3:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
