# List expression 2
Списочное выражение 2
На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет 
кубы указанных чисел также на одной строке.
Примечание 1. Для вывода элементов списка используйте цикл for.
Примечание 2. Используйте метод split().
# The input to the program is a text string containing integers. Write a program using a list expression that will print
# cubes of the indicated numbers are also on one line.
# Note 1: Use a for loop to display the elements of a list.
# Note 2: Use the split() method.

a = [int(a)**3 for a in input().split()]
print(*a)


Sample Input 1:
2 4 3
Sample Output 1:
8 64 27
Sample Input 2:
-2 -5 0
Sample Output 2:
-8 -125 0
