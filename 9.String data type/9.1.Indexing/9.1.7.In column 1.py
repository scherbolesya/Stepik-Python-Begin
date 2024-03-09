В столбик 1
# In column 1
На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
# One line is given as input to the program. Write a program that displays the elements of a string with indexes 0, 2, 4, ... in a column.

c = input() #Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
for i in range(0,len(c),2):
    print(c[i])


Sample Input:
abcdefghijklmnop

Sample Output:
a
c
e
g
i
k
m
o
