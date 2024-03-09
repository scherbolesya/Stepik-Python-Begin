# Characters in range
Символы в диапазоне
На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения в диапазоне от a до b (включительно), 
выводит соответствующий ему символ из таблицы символов Unicode.
# The program is given two numbers a and b as input. Write a program that, for each code value in the range from a to b (inclusive),
# displays the corresponding character from the Unicode character table.

a = int(input())
b = int(input())
for i in range(a,b+1):
    print(chr(i), end=' ')


Sample Input 1:
65
70
Sample Output 1:
A B C D E F
Sample Input 2:
97
110
Sample Output 2:
a b c d e f g h i j k l m n
Sample Input 3:
48
64
Sample Output 3:
0 1 2 3 4 5 6 7 8 9 : ; < = > ? @
