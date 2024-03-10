Google search - 1
На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. 
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
Примечание. Поиск не должен быть чувствителен к регистру символов.
# The input to the program is a natural number n, then n lines, then another line - a search query.
# Write a program that prints all entered lines that contain a search term.
# Note. The search should not be case sensitive.

n = int(input())
a = []
for i in range(n):
    s = input()
    #a1 = s.lower()
    a.append(s)
b = input()
for i in range(len(a)):
    if b.lower() in a[i].lower():
        print(a[i]) 


Sample Input:
5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
язык

Sample Output:
Язык Python прекрасен
C# - отличный язык программирования
язык Python появился 20 февраля 1991
