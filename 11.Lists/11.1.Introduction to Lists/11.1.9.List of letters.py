# List of letters
# The input to the program is one number n. Write a program that prints a list of n letters of the English alphabet ['a', 'b', 'c', ...] in lowercase.
Список букв
На вход программе подается одно число n. Напишите программу, которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

n = int(input()) #
a = 'abcdefghijklmnopqrstuvwxyz' #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = ''
for i in range(n):
    b = b + a[i]
print(list(b))

  
Sample Input 1:
1
Sample Output 1:
['a']
Sample Input 2:
5
Sample Output 2:
['a', 'b', 'c', 'd', 'e']
Sample Input 3:
10
Sample Output 3:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
