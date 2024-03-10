# One line 3
В одну строку 3
На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выводит не оканчивающиеся на цифру 4 квадраты четных чисел.
Примечание 1. Программу можно написать в одну строку кода.
Примечание 2. На цифру 4 не должны оканчиваться именно квадраты чисел, а не сами числа.
# The input to the program is a text string containing integers. Write a program using a list expression that prints squares of even numbers that do not end in 4.
# Note 1: The program can be written in one line of code.
# Note 2. It is the squares of numbers that should not end with the number 4, and not the numbers themselves.

print(*[int(i)**2 for i in input().split() if int(i)%2 == 0 and (int(i)**2)%10 != 4])

  
Sample Input 1:
1 2 3 4 5 6 7 8 9
Sample Output 1:
16 36
Sample Input 2:
4 4 10 6 4
Sample Output 2:
16 16 100 36 16
