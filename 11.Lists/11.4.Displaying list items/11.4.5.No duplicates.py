# No duplicates
Без дубликатов
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только уникальные строки, 
в том же порядке, в котором они были введены.
# The input to the program is a natural number n, and then n strings. Write a program that prints only unique strings,
# in the same order in which they were entered.

n = int(input())
a = []
for i in range(n):
    s = input()
    if s not in a:
        a.append(s)
    else:
        continue
print(*a, sep='\n')


Sample Input:
5
first
second
first
third
second

Sample Output:
first
second
third
