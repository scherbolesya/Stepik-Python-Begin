Самый частотный символ
# Most Frequent Symbol
На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
# A line of text is given as input to the program. Write a program that displays the symbol that appears most frequently.
# Note 1. If there are several such characters, the last character in order should be displayed.
# Note 2. It is necessary to distinguish between upper and lowercase letters, as well as letters of the Russian and English alphabet.

s = input()
x=0
a=0
for i in s:
    if s.count(i) > x or s.count(i) == x:
        x = s.count(i)
        a = i
print (a)

  
Sample Input 1:
aaaabbc
Sample Output 1:
a
Sample Input 2:
abaabbcccc
Sample Output 2:
c
