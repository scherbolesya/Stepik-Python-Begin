# List of strings
# The input to the program is a natural number n, and then n strings. Write a program that creates a list from the given strings and displays it.
Список строк
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.

a = int(input())
b = []
for i in range(a):
        b.append(str(input()))            
print(b)


Sample Input:
5
C#
C++
C
Python
F#
Sample Output:
['C#', 'C++', 'C', 'Python', 'F#']
