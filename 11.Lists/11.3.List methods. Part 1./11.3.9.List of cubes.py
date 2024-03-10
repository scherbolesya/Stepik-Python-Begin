# List of cubes
# The input to the program is a natural number n, and then n integers. Write a program that creates a list of their cubes from the given numbers.
Список кубов
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

a = []  
for i in range (int(input())):
    s = (int(input()))**3
    a.append(s)
print(a)

  
Sample Input 1:
5
1
2
3
4
5
Sample Output 1:
[1, 8, 27, 64, 125]
Sample Input 2:
2
-5
-2
Sample Output 2:
[-125, -8]
Sample Input 3:
1
100
Sample Output 3:
[1000000]
