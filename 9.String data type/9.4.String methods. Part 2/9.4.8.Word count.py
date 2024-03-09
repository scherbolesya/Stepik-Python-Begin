# Word count
Количество слов
На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом. Напишите программу, которая подсчитывает количество слов в ней.
Примечание 1. Строка текста не содержит пробелов в начале и конце.
Примечание 2. Используйте для решения задачи метод count.
# The input to the program is a string of text consisting of words separated by exactly one space. Write a program that counts the number of words in it.
# Note 1: The text line does not contain leading or trailing spaces.
# Note 2: Use the count method to solve the problem.

s = input() 
print(s.count(' ')+1)


Sample Input 1:
Hello world
Sample Output 1:
2
Sample Input 2:
Python
Sample Output 2:
1
Sample Input 3:
In 2010, someone paid 10k Bitcoin for two pizzas.
Sample Output 3:
9
