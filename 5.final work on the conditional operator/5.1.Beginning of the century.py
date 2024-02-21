# Beginning of the century
# Write a program that determines whether a year with a given number ends with two zeros. If the year is ending, then print "YES", otherwise print "NO".
# Начало столетия
# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».

a = int(input()) #проверка заканчиавется ли число на 2 нуля
b = a % 100
if b == 0:
    print("YES")
else:
    print("NO")

Sample Input 1:
2000
Sample Output 1:
YES
Sample Input 2:
1999
Sample Output 2:
NO
Sample Input 3:
3000
Sample Output 3:
YES
