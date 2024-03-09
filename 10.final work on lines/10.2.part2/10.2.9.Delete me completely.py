# Delete me completely
# A line of text is given as input to the program. Write a program that removes all occurrences of the "@" symbol.
Удали меня полностью
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».

s= input()
a = ''
for i in s:
    if i != '@':
        print(i, end='')
      

Sample Input 1:
123@1@@34
Sample Output 1:
123134
Sample Input 2:
@@
Sample Output 2:
