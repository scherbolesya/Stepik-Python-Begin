# Rearrange min and max
Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел. 
Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
Примечание. Используйте подходящие встроенные функции и списочные методы.
# The input to the program is a string of text containing various natural numbers. A list of numbers is formed from this string.
# Write a program that swaps the minimum and maximum elements of this list.
# Note. Use appropriate built-in functions and list methods.

a1 = [int(i) for i in input().split()]
a = list(a1)
b = a.index(min(a))
c = a.index(max(a))
a[b], a[c] = a[c], a[b]
print(' '.join((str(i)for i in a)))

  
Sample Input 1:
3 4 5 2 1
Sample Output 1:
3 4 1 2 5
Sample Input 2:
10 9 8 7 6 5 4 3 2 1
Sample Output 2:
1 9 8 7 6 5 4 3 2 10
Sample Input 3:
1 2
Sample Output 3:
2 1
Sample Input 4:
1
Sample Output 4:
1
