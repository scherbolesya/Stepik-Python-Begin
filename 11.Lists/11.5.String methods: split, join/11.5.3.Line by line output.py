Построчный вывод
# Line by line output
На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
# A line of text is given as input to the program. Write a program that displays the words of the entered string in a column.

s = input()
s1 = s.split()
print(*s1, sep='\n')


Sample Input:
У лукоморья дуб зеленый златая цепь на дубе том

Sample Output:
У
лукоморья
дуб
зеленый
златая
цепь
на
дубе
том
