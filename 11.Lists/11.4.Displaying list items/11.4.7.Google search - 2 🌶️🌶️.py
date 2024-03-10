Google search - 2 🌶️🌶️
На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k строк — поисковые запросы. 
Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.
Примечание. Поиск не должен быть чувствителен к регистру символов.
# The input to the program is a natural number n, then n lines, then number k - the number of search queries, then k lines - search queries.
# Write a program that prints all the entered strings that contain all the search terms at the same time.
# Note. The search should not be case sensitive.

n = int(input())
a = []
b = []
for i in range(n):
    s = input()
    a.append(s)
n1 = int(input())
for i in range(n1):
    s1 = input()
    for j in range(len(a)):
        if s1.lower() in a[j].lower():
            b.append(a[j])
    a = b
    b = []
print(*a, sep='\n')

  
Sample Input:
5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
2
язык
python

Sample Output:
Язык Python прекрасен
язык Python появился 20 февраля 1991
