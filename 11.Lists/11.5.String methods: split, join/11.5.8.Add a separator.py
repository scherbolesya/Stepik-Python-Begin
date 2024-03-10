# Add a separator
Добавь разделитель
На вход программе подается строка текста и строка-разделитель. Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.
# The input to the program is a text line and a separator line. Write a program that inserts a specified delimiter between each character of an input string of text.

n = input()
n1 = input()
n2 = n1.join(n)
print(n2)


Sample Input 1:
1234567
*
Sample Output 1:
1*2*3*4*5*6*7

Sample Input 2:
qwerty and password
**
Sample Output 2:
q**w**e**r**t**y** **a**n**d** **p**a**s**s**w**o**r**d
