В столбик 2
# In column 2
На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
# One line is given as input to the program. Write a program that displays the elements of a string in reverse order in a column.

s = input()  #Программа должна вывести в столбик элементы строки в обратном порядке. 
for i in range(len(s)-1,-1,-1):
    print(s[i])


Sample Input:
abc
Sample Output:
c
b
a
