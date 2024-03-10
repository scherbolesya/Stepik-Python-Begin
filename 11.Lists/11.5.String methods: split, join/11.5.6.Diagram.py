# Diagram
Диаграмма
На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.
# The input to the program is a text string containing integers. Write a program that builds a bar graph using given numbers.

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    print('+'*numbers[i])
  
  
Sample Input 1:
1 2 3 4 5
Sample Output 1:
+
++
+++
++++
+++++

Sample Input 2:
5 3 1 7 10 2
Sample Output 2:
+++++
+++
+
+++++++
++++++++++
++
