# Sorting numbers
Сортировка чисел
На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. 
Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 
# The input to the program is a text string containing integers. A list of numbers is formed from this string.
# Write a program that sorts and displays the given list first in ascending order and then in descending order.

b = input().split()  #
a = [int(a) for a in b]  #s = [int(i) for i in input().split()]
print(*sorted(a))
print(*sorted(a, reverse=True))


Sample Input:
4 5 1 2 3 8
Sample Output:
1 2 3 4 5 8
8 5 4 3 2 1
