# In one line 1
В одну строку 1
На вход программе подается строка текста, содержащая слова. Напишите программу, которая выводит слова введенной строки в столбик.
Примечание. Программу можно написать в одну строку кода.
# The input to the program is a line of text containing words. Write a program that displays the words of the entered string in a column.
# Note. The program can be written in one line of code.

print(*(input().split()), sep="\n")

  
Sample Input:
Умей ценить того кто без тебя не может

Sample Output:
Умей
ценить
того
кто
без
тебя
не
может
