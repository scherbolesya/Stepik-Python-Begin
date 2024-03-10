# One line 2
В одну строку 2
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
Примечание. Программу можно написать в одну строку кода.
# A line of text is given as input to the program. Write a program using a list expression that prints all the numeric characters of a given string.
# Note. The program can be written in one line of code.

print(''.join([i for i in input() if '0' <= i <= '9']))

  
Sample Input 1:
Число Pi примерно равно 3.1415
Sample Output 1:
31415
Sample Input 2:
123Python awesome!56
Sample Output 2:
12356
