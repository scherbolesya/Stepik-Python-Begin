# Simple cipher
Простой шифр
На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.
# A line of text is given as input to the program. Write a program that translates each of its characters into its corresponding code from the Unicode character table.

s = input()
for c in s:
    print(ord(c), end=' ')
  

Sample Input:
Hello world!
Sample Output:
72 101 108 108 111 32 119 111 114 108 100 33
